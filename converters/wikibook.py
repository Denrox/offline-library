"""A Wikibooks book, one page per chapter.

Chapters and their sections come from the book's navigation templates; each
template is a section and becomes a category. Chapter wikitext is fetched,
stripped of navigation templates and rendered by the MediaWiki API. Images
are dropped.

Params (sources.json): book, nav_templates, strip_templates (regex),
skip_pages, notice (optional text shown at the top of every page).
"""

import json
import re
import time
import urllib.parse
import urllib.request

from .lib.html2md import html_to_md

API = "https://en.wikibooks.org/w/api.php"
UA = "offline-library (https://github.com/Denrox/offline-library)"


def api(params, post=False):
    params = {**params, "format": "json", "formatversion": "2"}
    data = urllib.parse.urlencode(params).encode()
    req = (urllib.request.Request(API, data=data, headers={"User-Agent": UA}) if post
           else urllib.request.Request(f"{API}?{data.decode()}", headers={"User-Agent": UA}))
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def wikitext(titles):
    res = api({"action": "query", "prop": "revisions", "rvprop": "content",
               "rvslots": "main", "titles": "|".join(titles)})
    return {p["title"]: p["revisions"][0]["slots"]["main"]["content"]
            for p in res["query"]["pages"] if "revisions" in p}


def sections(book, templates):
    """[(section, [chapter, ...])]; a template's first link is the section page."""
    src = wikitext(templates)
    out = []
    for t in templates:
        links = re.findall(r"\[\[" + re.escape(book) + r"/([^|\]{}]+)\|", src.get(t, ""))
        links = list(dict.fromkeys(l.strip() for l in links))
        if links:
            title = "Appendices" if links[0].startswith("Appendix") else links[0]
            out.append((title, links))
    return out


def render(page, strip_templates):
    text = wikitext([page]).get(page)
    if text is None:
        return None
    text = re.sub(r"\{\{\s*(" + strip_templates + r")[^{}]*\}\}", "", text)
    res = api({"action": "parse", "title": page, "text": text, "contentmodel": "wikitext",
               "prop": "text", "disablelimitreport": "1", "disableeditsection": "1"}, post=True)
    return html_to_md(res["parse"]["text"], "https://en.wikibooks.org")


def build(out, source):
    p = source["params"]
    book, skip = p["book"], set(p.get("skip_pages", []))
    notice = f"> **Note:** {p['notice']}\n\n" if p.get("notice") else ""
    today = time.strftime("%Y-%m-%d")
    done = {}

    for section, chapters in sections(book, p["nav_templates"]):
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
