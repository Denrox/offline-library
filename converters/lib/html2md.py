"""Minimal HTML -> Markdown converter (stdlib only).

Covers the tags MedlinePlus summaries and MediaWiki-rendered pages actually
use: headings, paragraphs, lists, links, emphasis, tables (flattened to
lists), line breaks. Anything else contributes only its text.
"""

from html.parser import HTMLParser
import re

# Elements whose whole subtree is dropped (MediaWiki chrome, edit links,
# reference markers, navboxes, scripts).
SKIP_CLASSES = {
    "mw-editsection", "reference", "references", "reflist", "navbox",
    "noprint", "mw-empty-elt", "toc", "printfooter", "catlinks",
    "mw-jump-link", "metadata", "ambox", "thumbcaption", "magnify",
    # Wikipedia: "For other uses, see ..." notes, sidebars, boxes pointing to other wikis.
    "hatnote", "sidebar", "sistersitebox", "side-box", "portalbox",
}
SKIP_TAGS = {"script", "style", "sup", "noscript", "figure", "img"}
VOID_TAGS = {"br", "img", "hr", "meta", "link", "input", "wbr", "source"}


class _Converter(HTMLParser):
    def __init__(self, base_url=""):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.out = []
        self.skip_depth = 0
        self.stack = []          # open tags, for skip-depth bookkeeping
        self.lists = []          # "ul" / "ol" with counters
        self.href = None
        self.link_text = []
        self.in_pre = False

    # -- helpers ------------------------------------------------------------
    def _emit(self, s):
        if self.href is not None:
            self.link_text.append(s)
        else:
            self.out.append(s)

    def _block(self):
        self.out.append("\n\n")

    # -- parser callbacks ---------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        if tag not in VOID_TAGS:
            self.stack.append(tag)
        if self.skip_depth:
            if tag not in VOID_TAGS:
                self.skip_depth += 1
            return
        if tag in SKIP_TAGS or classes & SKIP_CLASSES or a.get("role") == "navigation":
            if tag not in VOID_TAGS:
                self.skip_depth = 1
            return

        if re.fullmatch(r"h[1-6]", tag):
            self._block()
            # Page title is the document's single "#"; source headings start at "##".
            self.out.append("#" * min(6, int(tag[1]) + 1) + " ")
        elif tag in ("p", "div", "table", "blockquote", "dl"):
            self._block()
        elif tag in ("ul", "ol"):
            self.lists.append([tag, 0])
            self.out.append("\n")
        elif tag == "li":
            depth = max(0, len(self.lists) - 1)
            if self.lists and self.lists[-1][0] == "ol":
                self.lists[-1][1] += 1
                bullet = f"{self.lists[-1][1]}."
            else:
                bullet = "-"
            self.out.append("\n" + "  " * depth + bullet + " ")
        elif tag == "tr":
            self.out.append("\n- ")
        elif tag in ("td", "th"):
            self.out.append(" ")
        elif tag in ("dt",):
            self.out.append("\n\n**")
        elif tag in ("dd",):
            # "**Term** — definition" after a <dt>; a bare <dd> (wiki ":" indent)
            # is just its own line.
            after_dt = "".join(self.out[-3:]).rstrip().endswith("**")
            self.out.append(" — " if after_dt else "\x00BR\x00")
        elif tag == "br":
            self._emit("\x00BR\x00")
        elif tag in ("b", "strong"):
            self._emit("**")
        elif tag in ("i", "em"):
            self._emit("*")
        elif tag == "pre":
            self.in_pre = True
            self.out.append("\n\n```\n")
        elif tag == "a":
            href = a.get("href")
            if href and not href.startswith("#"):
                if href.startswith("//"):
                    href = "https:" + href
                elif href.startswith("/"):
                    href = self.base_url + href
                # "(" and ")" would end a markdown link early: Bearing_(angle).
                self.href = href.replace("(", "%28").replace(")", "%29")
                self.link_text = []

    def handle_endtag(self, tag):
        if self.stack and tag in self.stack:
            # Pop up to and including the matching tag (tolerates sloppy HTML).
            while self.stack:
                t = self.stack.pop()
                if self.skip_depth:
                    self.skip_depth -= 1
                    if self.skip_depth == 0 and t == tag:
                        return
                if t == tag:
                    break
            if self.skip_depth:
                return
        elif self.skip_depth:
            return

        if re.fullmatch(r"h[1-6]", tag) or tag in ("p", "div", "table", "blockquote", "dl"):
            self._block()
        elif tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            if not self.lists:
                self._block()
        elif tag == "dt":
            if self.out:
                self.out[-1] = self.out[-1].rstrip()
            self.out.append("**")
        elif tag in ("b", "strong"):
            self._emit("**")
        elif tag in ("i", "em"):
            self._emit("*")
        elif tag == "pre":
            self.in_pre = False
            self.out.append("\n```\n\n")
        elif tag == "a" and self.href is not None:
            text = "".join(self.link_text).strip()
            href, self.href = self.href, None
            if text:
                self.out.append(f"[{text}]({href})")

    def handle_data(self, data):
        if self.skip_depth:
            return
        if not self.in_pre:
            data = re.sub(r"\s+", " ", data)
        self._emit(data)


def html_to_md(html, base_url=""):
    c = _Converter(base_url)
    c.feed(html)
    c.close()
    md = "".join(c.out)
    md = re.sub(r"\*\*\s*\*\*", "", md)            # empty bold
    md = re.sub(r"[ \t]+\n", "\n", md)             # trailing spaces (keeps "  \n" breaks below)
    md = re.sub(r"\n[ \t]+(?![-\d])", "\n", md)    # leading spaces outside list items
    md = re.sub(r"(?m)^(\s*(?:-|\d+\.)) {2,}", r"\1 ", md)  # "-  item" -> "- item"
    md = re.sub(r"\n{3,}", "\n\n", md)
    # Hard line breaks go in last, so the whitespace cleanup above can't eat them.
    md = re.sub(r"\s*\x00BR\x00\s*", "  \n", md)
    lines = [l for l in md.split("\n") if l.strip() not in ("-", "*")]
    return "\n".join(lines).strip() + "\n"
