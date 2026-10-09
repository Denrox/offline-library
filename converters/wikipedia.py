"""Hand-picked Wikipedia articles, grouped into categories.

Each article is fetched as wikitext and rendered by the MediaWiki API (see
lib/mediawiki.py: formulas kept as TeX, images dropped). Sections that are no
use offline (references, see also, external links, ...) are left out, and so
are any the source names in skip_sections. Links between the chosen articles
stay as links; every other link becomes its text.

Params (sources.json):
  sections       {"Category": ["Article title", ...]}; an article may be in several
  skip_sections  optional regex of further section headings to leave out (e.g. "History")
  notice         optional text shown at the top of every page
"""

import re
import time
import urllib.parse

from .lib.mediawiki import api, render

SITE = "https://en.wikipedia.org"
# Sections every article leaves out: lists of sources and links elsewhere.
ALWAYS_SKIP = (r"(General |Further |Cited |Other )?references|(Explanatory )?notes( and references)?|Note|Footnotes|"
               r"Citations|Sources( .*)?|.*bibliography|Further reading|Externals? links|Related links|See also|"
               r"Gallery|In popular culture|Notable .*")
HEADING_LINE = re.compile(r"^(#{2,6}) (.*)$")


def canonical(titles):
    """{requested title: canonical title} after normalization and redirects;
    missing articles are left out. A disambiguation page ("X may refer to") is
    refused: the source must name the article it means."""
    out, ambiguous = {}, []
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        q = api({"action": "query", "titles": "|".join(chunk), "redirects": "1",
                 "prop": "pageprops", "ppprop": "disambiguation"}, site=SITE)["query"]
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        red = {r["from"]: r["to"] for r in q.get("redirects", [])}
        present = {p["title"] for p in q["pages"] if not p.get("missing")}
        ambiguous += [p["title"] for p in q["pages"] if "disambiguation" in p.get("pageprops", {})]
        for t in chunk:
            c = red.get(norm.get(t, t), norm.get(t, t))
            if c in present:
                out[t] = c
    if ambiguous:
        raise SystemExit(f"disambiguation pages, name the article instead: {ambiguous}")
    return out


def drop_sections(md, skip):
    """Leave out every section whose heading matches `skip`, with its subsections."""
    out, cut = [], None
    for line in md.split("\n"):
        m = HEADING_LINE.match(line)
        if m:
            level = len(m[1])
            if cut is not None and level <= cut:
                cut = None
            if cut is None and skip.fullmatch(m[2].strip()):
                cut = level
        if cut is None:
            out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def url_of(title):
    return f"{SITE}/wiki/" + urllib.parse.quote(title.replace(" ", "_"))


def build(out, source):
    p = source["params"]
    skip = re.compile(ALWAYS_SKIP + (f"|{p['skip_sections']}" if p.get("skip_sections") else ""), re.I)
    notice = f"> **Note:** {p['notice']}\n\n" if p.get("notice") else ""
    requested = list(dict.fromkeys(t for titles in p["sections"].values() for t in titles))
    names = canonical(requested)
    missing = [t for t in requested if t not in names]
    if missing:
        raise SystemExit(f"not on Wikipedia: {missing}")

    categories, urls = {}, {}
    for section, titles in p["sections"].items():
        for t in titles:
            c = names[t]
            categories.setdefault(c, [])
            if section not in categories[c]:
                categories[c].append(section)
            urls.setdefault(c, {url_of(c)}).add(url_of(t))

    for title, cats in categories.items():
        body = render(title, "$^", site=SITE)
        time.sleep(0.5)  # be polite to the Wikimedia API
        body = drop_sections(body, skip)
        md = (f"# {title}\n\n{notice}{body}\n---\n\n"
              f"*Source: Wikipedia, {title} ({url_of(title)}), by Wikipedia contributors, CC BY-SA 4.0.*\n")
        out.page(title, md, cats, urls=sorted(urls[title]))
    return time.strftime("%Y-%m-%d")
