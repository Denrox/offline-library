"""A Wikibooks book, one page per chapter.

Chapters and their sections come from the book's navigation templates; each
template is a section and becomes a category. Chapter wikitext is fetched,
stripped of navigation templates and rendered by the MediaWiki API. Images
are dropped.

Params (sources.json): book, nav_templates, strip_templates (regex),
skip_pages, notice (optional text shown at the top of every page),
section_names (optional {"heading": "category"} renames).

A nav template can also be the book's own contents page: when it has
headings, every heading with chapter links under it is a section.

Formulas (<math>) are taken from the wikitext as TeX and written as $$...$$:
on a line of their own as a display block, otherwise inline. Single dollars
are left alone, so prices in plain text never turn into math.
"""

import json
import re
import time
import urllib.parse
import urllib.request

from .lib.html2md import html_to_md

API = "https://en.wikibooks.org/w/api.php"
UA = "offline-library (https://github.com/Denrox/offline-library)"


def api(params, post=False, attempts=4):
    params = {**params, "format": "json", "formatversion": "2"}
    data = urllib.parse.urlencode(params).encode()
    req = (urllib.request.Request(API, data=data, headers={"User-Agent": UA}) if post
           else urllib.request.Request(f"{API}?{data.decode()}", headers={"User-Agent": UA}))
    # A build makes hundreds of calls; ride out the API's occasional 502/503.
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except OSError:
            if attempt == attempts:
                raise
            time.sleep(15 * attempt)


def wikitext(titles):
    res = api({"action": "query", "prop": "revisions", "rvprop": "content",
               "rvslots": "main", "titles": "|".join(titles)})
    return {p["title"]: p["revisions"][0]["slots"]["main"]["content"]
            for p in res["query"]["pages"] if "revisions" in p}


HEADING = re.compile(r"(?m)^(=+)\s*(.*?)\s*\1\s*$")
MATH = re.compile(r"<math(\s[^>]*)?>(.*?)</math>", re.S | re.I)
MATH_TOKEN = re.compile(r"MATHTOKEN(\d+)X")


def chapter_links(book, text):
    links = re.findall(r"\[\[" + re.escape(book) + r"/([^|\]{}]+)\|", text)
    return list(dict.fromkeys(l.strip() for l in links))


def heading_title(text):
    text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    text = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", text)
    return re.sub(r"'{2,}", "", text).strip()


def sections(book, templates):
    """[(section, [chapter, ...])]: a contents page's headings, or else each
    template with its first link as the section page."""
    src = wikitext(templates)
    out = []
    for t in templates:
        text = src.get(t, "")
        parts = HEADING.split(text)
        if len(parts) > 1:
            # [before, level, heading, body, level, heading, body, ...]; text before
            # the first heading (intro, print-version links) is not a section.
            for heading, body in zip(parts[2::3], parts[3::3]):
                links = chapter_links(book, body)
                if links:
                    out.append((heading_title(heading), links))
            continue
        links = chapter_links(book, text)
        if links:
            title = "Appendices" if links[0].startswith("Appendix") else links[0]
            out.append((title, links))
    return out


def katex_tex(tex):
    """MediaWiki TeX that KaTeX does not take, rewritten to what it does."""
    tex = re.sub(r"\s+", " ", tex).strip()
    if tex.endswith("\\"):
        tex += " "  # a trailing "\ " (control space) must keep its space
    while re.search(r"\*\{\d+\}\{[^{}]*\}", tex):  # array column repeats: *{2}{rc}
        tex = re.sub(r"\*\{(\d+)\}\{([^{}]*)\}", lambda m: m[2] * int(m[1]), tex)
    tex = re.sub(r"\\mbox(?![A-Za-z])", r"\\text", tex)
    return re.sub(r"\\sgn(?![A-Za-z])", r"\\operatorname{sgn}", tex)


def restore_math(md, formulas):
    """Put the TeX back: a formula alone on its line is a display block."""
    def tex(i):
        return katex_tex(formulas[int(i)])

    # A dollar sign written next to a formula ("$<math>8.45</math>") goes inside it.
    for m in re.finditer(r"\$MATHTOKEN(\d+)X", md):
        formulas[int(m[1])] = "\\$" + formulas[int(m[1])]
    md = re.sub(r"\$(MATHTOKEN\d+X)", r"\1", md)
    # Formulas that touch (an image between them was dropped) need a space, or
    # "$$a$$$$b$$" reads as one broken formula.
    md = re.sub(r"(MATHTOKEN\d+X)(?=MATHTOKEN)", r"\1 ", md)

    lines = []
    for line in md.split("\n"):
        m = re.fullmatch(r"\s*MATHTOKEN(\d+)X[\s,.;:]*", line)
        if m and not re.match(r"\s*(?:-|\d+\.)\s", line):
            if lines and lines[-1].endswith("  "):
                lines[-1] = lines[-1].rstrip()
            lines += ["", "$$", tex(m[1]), "$$", ""]
        else:
            lines.append(MATH_TOKEN.sub(lambda m: f"$${tex(m[1])}$$", line))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def render(page, strip_templates):
    text = wikitext([page]).get(page)
    if text is None:
        return None
    text = re.sub(r"\{\{\s*(" + strip_templates + r")[^{}]*\}\}", "", text)
    formulas = []

    def stash(m):
        formulas.append(m[2])
        return f"MATHTOKEN{len(formulas) - 1}X"

    text = MATH.sub(stash, text)
    res = api({"action": "parse", "title": page, "text": text, "contentmodel": "wikitext",
               "prop": "text", "disablelimitreport": "1", "disableeditsection": "1"}, post=True)
    md = html_to_md(res["parse"]["text"], "https://en.wikibooks.org")
    return restore_math(md, formulas) if formulas else md


def build(out, source):
    p = source["params"]
    book, skip = p["book"], set(p.get("skip_pages", []))
    notice = f"> **Note:** {p['notice']}\n\n" if p.get("notice") else ""
    today = time.strftime("%Y-%m-%d")
    done = {}

    names = p.get("section_names", {})
    for section, chapters in sections(book, p["nav_templates"]):
        section = names.get(section, section)
        for chapter in chapters:
            if chapter in skip:
                continue
            if chapter not in done:
                page = f"{book}/{chapter}"
                body = render(page, p.get("strip_templates", "$^"))
                time.sleep(0.5)  # be polite to the Wikimedia API
                if not body or len(body.strip()) < 200:
                    done[chapter] = None  # section landing pages are empty
                    continue
                url = "https://en.wikibooks.org/wiki/" + urllib.parse.quote(page.replace(" ", "_"))
                done[chapter] = (
                    f"# {chapter}\n\n{notice}{body}\n---\n\n"
                    f"*Source: Wikibooks, {page} ({url}), by Wikibooks contributors, "
                    "CC BY-SA 4.0.*\n",
                    [],
                    url,
                )
            if done[chapter]:
                done[chapter][1].append(f"{book}: {section}")

    for chapter, entry in done.items():
        if entry:
            out.page(f"{book} - {chapter}", entry[0], entry[1], urls=[entry[2]])
    return today
