"""A Docusaurus documentation site, from its source repository: one page per
.md/.mdx file, grouped into categories by folder.

MDX is turned into plain markdown: front matter gives the title and the page's
web address; import lines go, imported partials (the site's shared blocks) are
put in place; tabs become bold labels over their content; ":::note" style
admonitions become quotes; React components go, except link cards, which
become links; images go (the readers show no images). Code blocks are left
exactly as they are. Links to other pages of the site that are in the source
stay links (lib/output.py makes them relative); every other link becomes its
text.

Params (sources.json):
  archive     URL of a .tar.gz of the repository
  docs_dir    the docs folder inside it, e.g. "docs"
  site_url    where the docs are served, e.g. "https://meshtastic.org/docs"
  categories  [["path/prefix", "Category"], ...]: a page goes to the first
              prefix it starts with; pages under no prefix are left out
  skip        optional regexes of paths (relative to docs_dir) to leave out
  title_prefix  optional text put before every page title
"""

import io
import posixpath
import re
import tarfile
import time
import urllib.request

UA = "offline-library (https://github.com/Denrox/offline-library)"
# A line that opens or closes a code block; ```code``` on one line does neither.
FENCE = re.compile(r"^\s*(```|~~~)(?!.*(```|~~~))")
ADMONITION = re.compile(r"^:::(\w+)\s*(.*)$")
LABELS = {"note": "Note", "tip": "Tip", "info": "Info", "important": "Important",
          "caution": "Caution", "warning": "Warning", "danger": "Danger"}


def fetch(url, attempts=4):
    for attempt in range(1, attempts + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except OSError:
            if attempt == attempts:
                raise
            time.sleep(15 * attempt)


def front_matter(text):
    """(fields, body): the YAML front matter's simple "key: value" lines."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fields = {}
    for line in m[1].split("\n"):
        kv = re.match(r"^(\w+):\s*(.*)$", line)
        if kv:
            fields[kv[1]] = kv[2].strip().strip("\"'")
    return fields, text[m.end():]


def page_url(site_url, rel, fields):
    """The address Docusaurus serves a doc at: its slug, or its folder path and id."""
    if fields.get("slug", "").startswith("/"):
        return site_url + fields["slug"].rstrip("/")
    folder, name = posixpath.split(posixpath.splitext(rel)[0])
    if name == "index":
        name = ""
    name = fields.get("slug") or fields.get("id") or name
    return "/".join(p for p in (site_url, folder, name) if p).rstrip("/")


def attr(tag, name):
    m = re.search(name + r"""\s*=\s*(?:"([^"]*)"|'([^']*)'|\{["']([^"']*)["']\})""", tag)
    return next((g for g in m.groups() if g is not None), None) if m else None


def tab_labels(tag):
    """{value: label} from <Tabs values={[{label: 'A', value: 'a'}, ...]}>."""
    out = {}
    for obj in re.findall(r"\{([^{}]*)\}", tag):
        label, value = attr(obj.replace(":", "="), "label"), attr(obj.replace(":", "="), "value")
        if value:
            out[value] = label or value
    return out


class Mdx:
    def __init__(self, site_url, page, partials):
        self.site_url, self.page, self.partials = site_url, page, partials

    def link(self, href):
        """An absolute address for a link written in the page."""
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            return href
        if href.startswith("/docs/"):
            return self.site_url + href[len("/docs"):]
        if href.startswith("/"):
            return self.site_url.rsplit("/docs", 1)[0] + href
        path = re.sub(r"\.mdx?(?=$|#)", "", href)
        return posixpath.normpath(posixpath.join(self.page + "/..", path)).replace("https:/", "https://")

    def convert(self, body, imports=None):
        imports = {} if imports is None else imports
        # Imports: partials to put in place later, everything else dropped.
        for m in re.finditer(r'^import\s+(\w+)\s+from\s+["\']@site/docs/([^"\']+)["\'];?\s*$', body, re.M):
            imports[m[1]] = m[2]
        # An export that defines a component runs to its closing bracket at the start of a line.
        body = re.sub(r"^export\s[^\n]*[({=>]\s*\n.*?^[)}\]];?\s*$", "", body, flags=re.M | re.S)
        body = re.sub(r"^(import|export)\s.*?;?\s*$", "", body, flags=re.M)
        body = re.sub(r"\{/\*.*?\*/\}|<!--.*?-->", "", body, flags=re.S)

        out, code, quote, tabs = [], False, False, {}
        lines = body.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            i += 1
            if FENCE.match(line):
                code = not code
            elif code:
                pass
            elif ADMONITION.match(line.strip()):
                m = ADMONITION.match(line.strip())
                out += ["", f"> **{m[2] or LABELS.get(m[1].lower(), m[1].title())}:**", ">"]
                quote = True
                continue
            elif line.strip() == ":::":
                out.append("")
                quote = False
                continue
            else:
                # A component tag can span lines: gather it up to its closing ">".
                if re.match(r"^\s*<[A-Za-z]", line) and ">" not in line:
                    while i < len(lines) and ">" not in line:
                        line += " " + lines[i].strip()
                        i += 1
                line = self.line(line, imports, tabs)
            out += [f"> {l}".rstrip() if quote else l for l in line.split("\n")]
        md = "\n".join(out)
        md = re.sub(r"<(Dark|ReactPlayer|FaqAccordion|QRCode)\b.*?</\1>", "", md, flags=re.S)
        return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"

    def line(self, line, imports, tabs):
        s = line.strip()
        # Partials: <LoRaRegions /> is replaced by its converted content.
        m = re.fullmatch(r"<(\w+)\s*/>", s)
        if m and m[1] in imports and imports[m[1]] in self.partials:
            return Mdx(self.site_url, self.page, self.partials).convert(self.partials[imports[m[1]]])
        if s.startswith("<Tabs"):
            tabs.clear()
            tabs.update(tab_labels(s))
            return ""
        if s.startswith("<TabItem"):
            value = attr(s, "value")
            label = attr(s, "label") or tabs.get(value, value)
            return f"\n**{label}**\n" if label else ""
        # Link cards: <InstallCard title="Debian" description="..." to="/docs/..." />
        if re.match(r"<[A-Z]\w*\b", s) and (attr(s, "to") or attr(s, "href")) and attr(s, "title"):
            desc = attr(s, "description")
            return f"- [{attr(s, 'title')}]({self.link(attr(s, 'to') or attr(s, 'href'))})" + (f" — {desc}" if desc else "")
        # Other components (and layout HTML): the tags go, any text between them stays.
        line = re.sub(r"</?[A-Z]\w*\b[^<>]*?/?>", "", line)
        line = re.sub(r"^\s*<h([1-6])\b[^>]*>(.*?)</h\1>\s*$", lambda m: "#" * int(m[1]) + " " + m[2], line)
        line = re.sub(r"</?(div|span|br|wbr|center|p|img|details|summary|a|button|input|form|label|table|thead|tbody|"
                      r"tr|td|th|iframe|object|video|source|svg|path|figure|figcaption|picture|sup|sub|strong|em|b|i)\b[^<>]*?/?>",
                      "", line)
        # A table that was indented inside a component would read as code.
        if re.match(r"^\s+\|", line):
            line = line.lstrip()
        line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)
        return re.sub(r"\]\(([^)\s]+)\)", lambda m: f"]({self.link(m[1])})", line)


def build(out, source):
    p = source["params"]
    data = fetch(p["archive"])
    skip = [re.compile(r) for r in p.get("skip", [])]
    docs, partials = {}, {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        for m in tar.getmembers():
            parts = m.name.split("/", 1)
            if not m.isfile() or len(parts) < 2 or not parts[1].startswith(p["docs_dir"] + "/"):
                continue
            rel = parts[1][len(p["docs_dir"]) + 1:]
            if not rel.endswith((".md", ".mdx")):
                continue
            text = tar.extractfile(m).read().decode("utf-8")
            if posixpath.basename(rel).startswith("_"):
                partials[rel] = front_matter(text)[1]
            elif not any(r.search(rel) for r in skip):
                docs[rel] = text

    titles = set()
    for rel in sorted(docs):
        category = next((c for prefix, c in p["categories"] if rel.startswith(prefix)), None)
        if not category:
            continue
        fields, body = front_matter(docs[rel])
        url = page_url(p["site_url"], rel, fields)
        body = Mdx(p["site_url"], url, partials).convert(body)
        if len(body) < 200:
            continue  # landing pages with nothing but cards or links
        title = fields.get("title") or posixpath.basename(posixpath.splitext(rel)[0]).replace("-", " ").title()
        if title.lower() in titles:
            title = f"{title} ({posixpath.basename(posixpath.dirname(rel)).replace('-', ' ')})"
        titles.add(title.lower())
        title = p.get("title_prefix", "") + title
        md = (f"# {title}\n\n{body}\n---\n\n"
              f"*Source: {source['title']}, {url}. {source['license']}*\n")
        out.page(title, md, [category], urls=[url])
    return time.strftime("%Y-%m-%d")
