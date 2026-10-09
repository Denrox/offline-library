"""The MediaWiki API (Wikibooks, Wikipedia): wikitext, rendering to markdown,
formulas kept as TeX.

Formulas (<math>) are taken from the wikitext as TeX and written as $$...$$:
on a line of their own as a display block, otherwise inline. Single dollars
are left alone, so prices in plain text never turn into math.
"""

import json
import re
import time
import urllib.parse
import urllib.request

from .html2md import html_to_md

WIKIBOOKS = "https://en.wikibooks.org"
UA = "offline-library (https://github.com/Denrox/offline-library)"


def api(params, post=False, attempts=4, site=WIKIBOOKS):
    url = f"{site}/w/api.php"
    params = {**params, "format": "json", "formatversion": "2"}
    data = urllib.parse.urlencode(params).encode()
    req = (urllib.request.Request(url, data=data, headers={"User-Agent": UA}) if post
           else urllib.request.Request(f"{url}?{data.decode()}", headers={"User-Agent": UA}))
    # A build makes hundreds of calls; ride out the API's occasional 502/503.
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except OSError:
            if attempt == attempts:
                raise
            time.sleep(15 * attempt)


def wikitext(titles, site=WIKIBOOKS):
    res = api({"action": "query", "prop": "revisions", "rvprop": "content",
               "rvslots": "main", "titles": "|".join(titles)}, site=site)
    return {p["title"]: p["revisions"][0]["slots"]["main"]["content"]
            for p in res["query"]["pages"] if "revisions" in p}


MATH = re.compile(r"<math(\s[^>]*)?>(.*?)</math>", re.S | re.I)
MATH_TOKEN = re.compile(r"MATHTOKEN(\d+)X")


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


def render(page, strip_templates, site=WIKIBOOKS):
    text = wikitext([page], site).get(page)
    if text is None:
        return None
    text = re.sub(r"\{\{\s*(" + strip_templates + r")[^{}]*\}\}", "", text)
    formulas = []

    def stash(m):
        formulas.append(m[2])
        return f"MATHTOKEN{len(formulas) - 1}X"

    text = MATH.sub(stash, text)
    res = api({"action": "parse", "title": page, "text": text, "contentmodel": "wikitext",
               "prop": "text", "disablelimitreport": "1", "disableeditsection": "1"}, post=True, site=site)
    md = html_to_md(res["parse"]["text"], site)
    return restore_math(md, formulas) if formulas else md
