"""Over-the-counter drug labels from openFDA (FDA "Drug Facts", public domain).

All human OTC labels are paged from the openFDA API. Homeopathic products and
labels without uses, directions and warnings are left out. Labels are grouped by active ingredients and route (hundreds of store
brands share one ingredient); each group becomes one page built from its most
complete current adult label, listing the brand names it is sold under.
Categories come from the label's "Purpose".
"""

import collections
import html
import json
import re
import time
import urllib.parse
import urllib.request

from .lib.html2md import html_to_md

API = "https://api.fda.gov/drug/label.json"
UA = "offline-library (https://github.com/Denrox/offline-library)"
HOMEOPATHIC = re.compile(r"\bHPUS\b|homo?eopath|\b\d+\s?(X|C|CH|CK|LM|DH)\b", re.I)
WARNING_FIELDS = ("warnings", "do_not_use", "ask_doctor", "stop_use", "keep_out_of_reach_of_children")

# Drug Facts order: (label field, heading, leading words the field repeats).
SECTIONS = [
    ("active_ingredient", "Active ingredients", r"active ingredients?( \(in each [^)]*\))?"),
    ("purpose", "Purpose", r"purposes?"),
    ("indications_and_usage", "Uses", r"uses?|indications?( and usage)?"),
    ("warnings", "Warnings", r"warnings?"),
    ("do_not_use", "Do not use", r"do not use"),
    ("ask_doctor", "Ask a doctor before use if", r"ask a doctor before use( if)?"),
    ("ask_doctor_or_pharmacist", "Ask a doctor or pharmacist before use if",
     r"ask a doctor or pharmacist before use( if)?"),
    ("when_using", "When using this product", r"when using this product"),
    ("stop_use", "Stop use and ask a doctor if", r"stop use and ask a doctor( if)?"),
    ("pregnancy_or_breast_feeding", "Pregnancy or breast-feeding", r""),
    ("keep_out_of_reach_of_children", "Keep out of reach of children", r""),
    ("dosage_and_administration", "Directions", r"directions?|dosage and administration"),
    ("storage_and_handling", "Other information", r"other information|storage and handling"),
    ("inactive_ingredient", "Inactive ingredients", r"inactive ingredients?"),
]
KEEP = {f for f, _, _ in SECTIONS} | {f"{f}_table" for f, _, _ in SECTIONS} | {"openfda", "effective_time", "set_id"}

# Purpose wording -> everyday category; first match wins, a label can match several.
CATEGORIES = [
    ("Sunscreens", r"sunscreen|sun protect"),
    ("Smoking cessation", r"stop smoking|smoking cessation|nicotine"),
    ("Sleep aids", r"sleep|nighttime"),
    ("Cold, cough and allergy", r"antihistamine|decongestant|cough|expectorant|cold|allerg|sore throat|oral anesthetic"),
    ("Pain and fever", r"pain reliever|fever|analgesic(?! .*(topical|external))|headache"),
    ("Topical pain relief", r"topical analgesic|external analgesic|topical anesthetic|counterirritant|local anesthetic"),
    ("Digestive health", r"antacid|acid reducer|laxative|stool soften|antidiarr|anti-diarr|antiemetic|nausea|gas|antiflatulent|hemorrhoid"),
    ("Antiseptics and hand sanitizers", r"antiseptic|antibacterial|antimicrobial|hand sanit|first aid"),
    ("Antifungals", r"antifungal|athlete|ringworm|jock itch|yeast"),
    ("Acne", r"acne"),
    ("Dandruff and scalp", r"dandruff|seborrheic|psoriasis"),
    ("Skin protectants", r"skin protectant|diaper|anti-itch|itch|poison ivy|insect bite|astringent"),
    ("Warts, corns and calluses", r"wart|corn|callus"),
    ("Oral care", r"anticavity|cavity|gingivitis|antiplaque|plaque|sensitivity|tooth|fluoride"),
    ("Eye care", r"eye|ophthalmic|lubricant drops"),
    ("Antiperspirants", r"antiperspirant"),
    ("Lice", r"lice|pediculicide"),
    ("Hair loss", r"hair regrowth|hair growth|hair loss|minoxidil"),
    ("Ear care", r"earwax|ear wax|\bear\b"),
    ("Insect repellents", r"repellent|mosquito"),
    ("Asthma", r"bronchodilator|asthma"),
]

# When the purpose names no category, the route can.
ROUTE_CATEGORIES = {"OPHTHALMIC": "Eye care", "DENTAL": "Oral care", "NASAL": "Cold, cough and allergy",
                    "RESPIRATORY (INHALATION)": "Asthma", "AURICULAR (OTIC)": "Ear care"}
NO_INFO = re.compile(r"see the (enclosed )?leaflet|read the enclosed|see (the )?package insert", re.I)


def fetch_all(product_type):
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
            yield {k: v for k, v in rec.items() if k in KEEP}, meta
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
    """Section text without its repeated heading, with "•" items as a list."""
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
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip()
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


def categories_for(rec, routes):
    purpose = (text(rec, "purpose") or text(rec, "indications_and_usage")[:300]).lower()
    found = [name for name, pattern in CATEGORIES if re.search(pattern, purpose)]
    found = found or [ROUTE_CATEGORIES[r] for r in routes if r in ROUTE_CATEGORIES]
    return found or ["Other"]


def form_key(rec):
    """Active-ingredient wording without spacing/punctuation: same strength and form."""
    return re.sub(r"[^a-z0-9]", "", text(rec, "active_ingredient").lower())[:80]


def for_children(rec):
    brands = " ".join(rec.get("openfda", {}).get("brand_name", [])).lower()
    directions = text(rec, "dosage_and_administration").lower()
    return bool(re.search(r"child|infant|junior|kid|pediatric|baby", brands)
                or re.search(r"weight \(lb\)|right dose on (the )?chart|dosing (cup|syringe)", directions))


def score(rec, common_form=None):
    """Prefer complete adult labels of the most common adult form, then the newest."""
    s = sum(1 for f, _, _ in SECTIONS if has(rec, f))
    if "adult" in text(rec, "dosage_and_administration").lower():
        s += 3
    if for_children(rec):
        s -= 5
    return (s, form_key(rec) == common_form, rec.get("effective_time", ""))


def build(out, source):
    p = source.get("params", {})
    groups = collections.defaultdict(list)
    meta = {}
    for rec, meta in fetch_all(p.get("product_type", "HUMAN OTC DRUG")):
        o = rec.get("openfda", {})
        subs = tuple(sorted(set(o.get("substance_name", []))))
        probe = " ".join(text(rec, f) for f in ("active_ingredient", "purpose")) + text(rec, "indications_and_usage")[:300]
        if not subs or HOMEOPATHIC.search(probe):
            continue
        # Only real Drug Facts labels: uses, directions and warnings.
        if not (has(rec, "indications_and_usage") and has(rec, "dosage_and_administration")
                and any(has(rec, f) for f in WARNING_FIELDS)):
            continue
        if NO_INFO.search(text(rec, "indications_and_usage")[:200] + " " + text(rec, "purpose")[:200]):
            continue
        routes = tuple(sorted(o.get("route", []))) or ("UNKNOWN",)
        groups[(subs, routes)].append(rec)

    routes_per_combo = collections.Counter(subs for subs, _ in groups)
    notice = f"> **Note:** {p['notice']}\n\n" if p.get("notice") else ""

    for (subs, routes), recs in groups.items():
        adult = [r for r in recs if not for_children(r)] or recs
        common_form = collections.Counter(form_key(r) for r in adult).most_common(1)[0][0]
        rep = max(recs, key=lambda r: score(r, common_form))
        name = join_names(subs)
        title = name
        if routes_per_combo[subs] > 1:
            title += f" ({', '.join(r.lower() for r in routes)})"

        brands = collections.Counter()
        for r in recs:
            for b in r.get("openfda", {}).get("brand_name", []):
                b = re.sub(r"\s+", " ", b).strip()
                if b and b.lower() != name.lower():
                    brands[title_case(b)] += 1
        o = rep.get("openfda", {})

        parts = [f"# {title}\n", notice.rstrip("\n") + "\n" if notice else ""]
        facts = [f"**Route:** {', '.join(r.lower() for r in routes)}"]
        if o.get("pharm_class_epc"):
            classes = [re.sub(r"\s*\[EPC\]$", "", c) for c in o["pharm_class_epc"]]
            facts.append(f"**Drug class:** {', '.join(classes)}")
        facts.append(f"**Labels on file:** {len(recs)}")
        parts.append("  \n".join(facts) + "\n")
        if brands:
            # Real brand names (Advil, Motrin IB) before store generics ("Equate Ibuprofen").
            words = {w for s in subs for w in s.lower().split()}
            ranked = sorted(brands.items(), key=lambda kv: (bool(words & set(kv[0].lower().split())), -kv[1]))
            top = [b for b, _ in ranked[:25]]
            more = len(brands) - len(top)
            parts.append("**Also sold as:** " + ", ".join(top) + (f" and {more} more" if more > 0 else "") + "\n")

        for field, heading, lead in SECTIONS:
            content = text(rep, field)
            if not has(rep, field):
                continue
            level = "###" if field in ("do_not_use", "ask_doctor", "ask_doctor_or_pharmacist", "when_using",
                                       "stop_use", "pregnancy_or_breast_feeding",
                                       "keep_out_of_reach_of_children") else "##"
            section = body(content, lead)
            table = rep.get(f"{field}_table")
            if table:
                section += "\n\n" + "\n\n".join(table_md(t) for t in table)
            parts.append(f"{level} {heading}\n\n{section}\n")

        date = rep.get("effective_time", "")
        date = f"{date[:4]}-{date[4:6]}-{date[6:8]}" if len(date) == 8 else "unknown date"
        parts.append(
            f"---\n\n*Source: FDA drug label via openFDA, label effective {date}, "
            f"DailyMed set ID {rep.get('set_id', 'unknown')}. Public domain.*\n"
        )
        out.page(title, "\n".join(x for x in parts if x), categories_for(rep, routes))

    return meta.get("last_updated", time.strftime("%Y-%m-%d"))
