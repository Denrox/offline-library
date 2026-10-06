"""Shared helpers for converters built on openFDA drug labels.

Labels are streamed from the API and grouped by active ingredients and route;
only the best label per group and form is kept in memory, since there are tens
of thousands of labels and prescription labels are large.
"""

import collections
import html
import json
import re
import time
import urllib.parse
import urllib.request

from .html2md import html_to_md

API = "https://api.fda.gov/drug/label.json"
UA = "offline-library (https://github.com/Denrox/offline-library)"
# Words that make a product name generic rather than a brand.
GENERIC_WORDS = {"hcl", "hydrochloride", "sodium", "potassium", "calcium", "usp", "tablets", "tablet", "capsules",
                 "capsule", "oral", "solution", "suspension", "injection", "cream", "ointment", "gel", "er", "xr",
                 "sr", "dr", "extended", "delayed", "release", "and", "mg", "film", "coated", "chewable", "drops",
                 "spray", "topical", "liquid", "syrup", "for", "of", "in", "with"}


def fetch_all(product_type, keep):
    """Yield (label limited to `keep` fields, response meta) for every label of a product type."""
    url = f"{API}?" + urllib.parse.urlencode({"search": f'openfda.product_type:"{product_type}"', "limit": 1000})
    meta = {}
    while url:
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=120) as r:
                    body, link = json.load(r), r.headers.get("Link", "")
                break
            except OSError:
                if attempt == 4:
                    raise
                time.sleep(15 * (attempt + 1))
        meta = body.get("meta", meta)
        for rec in body["results"]:
            yield {k: v for k, v in rec.items() if k in keep}, meta
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None


def text(rec, field):
    value = rec.get(field)
    return " ".join(value).strip() if isinstance(value, list) else ""


def has(rec, field):
    return len(text(rec, field)) >= 10


def title_case(name):
    small = {"and", "of", "with", "in"}
    return " ".join(w if w in small else w.capitalize() for w in name.lower().split())


def join_names(names):
    names = [title_case(n) for n in names]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def body(field_text, lead):
    """Section text without its repeated heading, with bullet items as a list."""
    t = re.sub(r"\s+", " ", field_text).strip()
    if lead:
        t = re.sub(rf"^(?:{lead})\s*:?\s*", "", t, flags=re.I)
    parts = [p.strip(" ;") for p in re.split(r"\s*[•■●▪◦◆►]\s*", t)]
    head, items = parts[0], [p for p in parts[1:] if p]
    lines = [head] if head else []
    if items:
        lines.append("\n".join(f"- {i}" for i in items))
    return "\n\n".join(lines)


def table_md(fragment):
    """A label's HTML table as a markdown table; full-width rows become captions."""
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", fragment, flags=re.S | re.I)
    grid, captions = [], []
    for row in rows:
        cells = [re.sub(r"\s*\(\s*(,\s*)*\)", "", re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c)))).strip()
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, flags=re.S | re.I)]
        if len(cells) == 1 or (cells and all(not c for c in cells[1:])):
            if cells[0]:
                captions.append(cells[0])
        elif cells:
            grid.append([c.replace("|", "/") for c in cells])
    if not grid:
        return html_to_md(fragment)
    width = max(len(r) for r in grid)
    grid = [r + [""] * (width - len(r)) for r in grid]
    md = [f"| {' | '.join(grid[0])} |", "|" + " --- |" * width] + [f"| {' | '.join(r)} |" for r in grid[1:]]
    return "\n\n".join([f"**{c}**" for c in captions] + ["\n".join(md)])


def form_key(rec):
    """Active-ingredient wording without spacing/punctuation: same strength and form."""
    return re.sub(r"[^a-z0-9]", "", text(rec, "active_ingredient").lower())[:80]


class Group:
    """Labels sharing ingredients and route: brand counts, and the best label per form."""

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.brands = collections.Counter()
        self.classes = collections.Counter()     # FDA drug classes across all labels
        self.substances = collections.Counter()  # exact ingredient forms ("Atorvastatin Calcium Trihydrate")
        self.forms = collections.Counter()      # forms of preferred (e.g. adult) labels
        self.all_forms = collections.Counter()
        self.best = {}                          # form -> ((score, effective_time), label)

    def add(self, rec, score, form, preferred=True):
        self.count += 1
        for b in rec.get("openfda", {}).get("brand_name", []):
            b = re.sub(r"\s+", " ", b).strip()
            if b and b.lower() != self.name.lower():
                self.brands[title_case(b)] += 1
        for sub in rec.get("openfda", {}).get("substance_name", []):
            self.substances[title_case(sub)] += 1
        for c in rec.get("openfda", {}).get("pharm_class_epc", []):
            self.classes[re.sub(r"\s*\[EPC\]$", "", c)] += 1
        self.all_forms[form] += 1
        if preferred:
            self.forms[form] += 1
        key = (score, rec.get("effective_time", ""))
        if form not in self.best or key > self.best[form][0]:
            self.best[form] = (key, rec)

    def representative(self):
        """Best score, then the most common form, then the newest label."""
        common = (self.forms or self.all_forms).most_common(1)[0][0]
        form, ((score, date), rec) = max(self.best.items(),
                                         key=lambda item: (item[1][0][0], item[0] == common, item[1][0][1]))
        return rec

    def brand_names(self, subs, limit=25):
        """Real brand names (Advil) before store generics ("Equate Ibuprofen"); names
        that only repeat the ingredient, salt and form ("Sertraline Hcl") are left out."""
        words = {w for s in list(subs) + list(self.substances) for w in re.findall(r"[a-z]+", s.lower())}
        brands = [(b, n) for b, n in self.brands.items()
                  if not set(re.findall(r"[a-z]+", b.lower())) <= words | GENERIC_WORDS | SALT_WORDS]
        ranked = sorted(brands, key=lambda kv: (bool(words & set(kv[0].lower().split())), -kv[1]))
        return [b for b, _ in ranked[:limit]], max(0, len(brands) - limit)


# Salt, ester and hydrate words: "ATORVASTATIN CALCIUM TRIHYDRATE" is atorvastatin.
SALT_WORDS = {"calcium", "sodium", "potassium", "magnesium", "hydrochloride", "hcl", "dihydrochloride", "hydrobromide",
              "sulfate", "bisulfate", "maleate", "mesylate", "besylate", "tartrate", "bitartrate", "citrate", "acetate",
              "phosphate", "diphosphate", "succinate", "fumarate", "hemifumarate", "malate", "tosylate", "lactate",
              "gluconate", "bromide", "chloride", "nitrate", "oxalate", "pamoate", "valerate", "propionate",
              "dipropionate", "furoate", "butyrate", "hyclate", "monohydrate", "dihydrate", "trihydrate",
              "sesquihydrate", "hemihydrate", "anhydrous", "hydrate", "propylene", "glycol", "solvate", "salt",
              "disodium", "dipotassium", "monosodium", "tromethamine", "meglumine", "free", "base"}


# A leading metal is the active ingredient itself (calcium carbonate, sodium fluoride).
CATIONS = {"calcium", "sodium", "potassium", "magnesium", "ferrous", "ferric", "zinc", "aluminum", "lithium",
           "silver", "copper", "barium", "ammonium", "bismuth", "selenium", "strontium", "iron"}


def base_name(substance):
    """Drug name without its salt/hydrate words ("ATORVASTATIN CALCIUM TRIHYDRATE" -> "ATORVASTATIN");
    mineral compounds ("CALCIUM CARBONATE", "POTASSIUM CHLORIDE") are kept whole."""
    words = substance.split()
    if not words or words[0].lower() in CATIONS:
        return substance
    core = [words[0]] + [w for w in words[1:] if w.lower().strip(",()") not in SALT_WORDS]
    return " ".join(core)


def group_key(rec):
    o = rec.get("openfda", {})
    subs = tuple(sorted({base_name(s) for s in o.get("substance_name", [])}))
    routes = tuple(sorted(o.get("route", []))) or ("UNKNOWN",)
    return subs, routes


def label_date(rec):
    d = rec.get("effective_time", "")
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) == 8 else "unknown date"
