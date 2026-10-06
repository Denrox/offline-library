"""MedlinePlus health topics (U.S. National Library of Medicine).

Downloads the newest health-topics XML listed on https://medlineplus.gov/xml.html
(published Tuesday to Saturday) and writes one page per English topic.
MedlinePlus "groups" become categories.
"""

import re
import urllib.request
import xml.etree.ElementTree as ET

from .lib.html2md import html_to_md

INDEX_URL = "https://medlineplus.gov/xml.html"
UA = "offline-library (https://github.com/Denrox/offline-library)"


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
        return r.read()


def latest_xml_url():
    html = fetch(INDEX_URL).decode("utf-8", "replace")
    urls = sorted(set(re.findall(r"https://medlineplus\.gov/xml/mplus_topics_\d{4}-\d{2}-\d{2}\.xml", html)))
    if not urls:
        raise RuntimeError(f"no health-topics XML linked from {INDEX_URL}")
    return urls[-1]


def build(out, source, xml_path=None):
    data = open(xml_path, "rb").read() if xml_path else fetch(latest_xml_url())
    root = ET.fromstring(data)
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", root.get("date-generated", ""))
    snapshot = f"{m[3]}-{m[1]}-{m[2]}" if m else "unknown"

    for t in root.findall("health-topic"):
        if t.get("language") != "English":
            continue
        title = t.get("title").strip()
        also = [a.text.strip() for a in t.findall("also-called") if a.text]
        groups = [g.text.strip() for g in t.findall("group") if g.text]
        related = [r.text.strip() for r in t.findall("related-topic") if r.text]

        parts = [f"# {title}\n"]
        if also:
            parts.append(f"*Also called: {', '.join(also)}*\n")
        parts.append(html_to_md(t.findtext("full-summary") or "", "https://medlineplus.gov"))
        if related:
            parts.append("## Related topics\n\n" + "\n".join(f"- {r}" for r in related) + "\n")
        parts.append(
            f"---\n\n*Source: [MedlinePlus]({t.get('url')}), U.S. National Library of "
            "Medicine. General information, not medical advice.*\n"
        )
        out.page(title, "\n".join(parts), groups)

    return snapshot
