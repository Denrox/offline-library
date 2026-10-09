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

Formulas are kept as TeX (see lib/mediawiki.py).
"""

import re
import time
import urllib.parse

from .lib.mediawiki import render, wikitext

HEADING = re.compile(r"(?m)^(=+)\s*(.*?)\s*\1\s*$")


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
