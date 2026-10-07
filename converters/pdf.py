"""A PDF manual, one page per chapter.

Text comes from pymupdf4llm (headings, lists, bold). Chapters start where a
line matches `chapter`; the heading after it is the chapter title. Parts
(optional `part` regex, title on the next heading) become categories.
Images are dropped; figure captions stay.

Params (sources.json):
  url            PDF to download
  name           short name, used as the file-name prefix
  first_page, last_page   1-based page range holding the chapters
  header, footer points to blank at the top and bottom of every page
  chapter, part  regexes matched against markdown lines
  strip          regexes removed from heading text (e.g. bookmark labels)
  extra_pages    [{"title", "first", "last", "category"}] kept as single pages
  notice         optional text shown at the top of every page
  repair_initials  restore a first letter the PDF's text layer lost in headings
                 (e.g. small-caps "LOOD" -> "BLOOD"), using the body's vocabulary
"""

import collections
import re
import time
import urllib.request

import pymupdf
import pymupdf4llm

UA = "offline-library (https://github.com/Denrox/offline-library)"
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


def fetch(url, attempts=3):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except OSError:
            if attempt == attempts:
                raise
            time.sleep(30 * attempt)


def blank_margins(doc, header, footer):
    for page in doc:
        w, h = page.rect.width, page.rect.height
        if header:
            page.add_redact_annot(pymupdf.Rect(0, 0, w, header))
        if footer:
            page.add_redact_annot(pymupdf.Rect(0, h - footer, w, h))
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                              graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)


def clean(markdown, strip):
    out = []
    for line in markdown.splitlines():
        if line.strip() in ("This page intentionally left blank.", "**This page intentionally left blank.**"):
            continue
        m = HEADING.match(line.strip())
        if m:
            text = re.sub(r"\s+", " ", m[2].replace("**", "")).strip()
            for pattern in strip:
                text = re.sub(pattern, "", text).strip()
            line = f"{m[1]} {text}"
        # Bullets drawn in a symbol font have no Unicode mapping: drop them after a
        # list marker, make the rest (bulleted items inside table cells) real bullets.
        line = re.sub(r"^(\s*[-*]\s+)�\s*", r"\1", line)
        line = re.sub(r"�\s*", "• ", line)
        out.append(line.rstrip())
    return out


def heading_text(line):
    m = HEADING.match(line)
    return m[2].strip() if m else None


def tidy(lines):
    text = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


class Headings:
    """Heading clean-up that needs the document's body text."""

    SMALL = {"and", "or", "of", "the", "for", "to", "in", "on", "a", "an", "with", "by", "at", "from"}

    def __init__(self, body_lines, repair_initials):
        words = [w for line in body_lines for w in re.findall(r"[A-Za-z]+", line)]
        # Words seen in normal writing; all-caps text can carry the same damage as headings.
        self.counts = collections.Counter(w.lower() for w in words if not w.isupper())
        self.vocab = set(self.counts)
        # Acronyms (TQ, CUF, TCCC) appear in capitals and never in lower case.
        self.acronyms = {w for w in words if len(w) > 1 and w.isupper() and w.lower() not in self.vocab}
        self.repair = repair_initials

    def _repair_word(self, word):
        if not self.repair or len(word) < 3 or word.lower() in self.vocab:
            return word
        if not (word.isupper() or word.islower()):
            return word
        found = sorted(((self.counts[(c + word).lower()], c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        if (c + word).lower() in self.vocab), reverse=True)
        # Only a clear winner: "blood" (hundreds of uses) over "flood" (one).
        if not found or (len(found) > 1 and found[0][0] < 3 * found[1][0]):
            return word
        return found[0][1] + word

    def fix(self, text):
        text = re.sub(r"[A-Za-z]+", lambda m: self._repair_word(m.group()), text)
        if text != text.upper():
            return text
        out = []
        for i, word in enumerate(text.split()):
            core = re.sub(r"[^A-Za-z]", "", word)
            if core in self.acronyms:
                out.append(word)
            elif i and word.lower() in self.SMALL:
                out.append(word.lower())
            else:
                out.append(word[:1] + word[1:].lower())
        return " ".join(out)

    def render(self, lines):
        """Our page title is the only H1; the levels a page uses become H2, H3, ..."""
        levels = sorted({len(m[1]) for m in map(HEADING.match, lines) if m})
        rank = {level: min(i + 2, 6) for i, level in enumerate(levels)}
        out = []
        for line in lines:
            m = HEADING.match(line)
            out.append(f"{'#' * rank[len(m[1])]} {self.fix(m[2])}" if m else line)
        return tidy(out)


def build(out, source):
    p = source["params"]
    doc = pymupdf.open(stream=fetch(p["url"]), filetype="pdf")
    blank_margins(doc, p.get("header", 0), p.get("footer", 0))
    strip = p.get("strip", [])
    chapter_re = re.compile(p["chapter"])
    part_re = re.compile(p["part"]) if p.get("part") else None
    notice = f"> **Note:** {p['notice']}\n\n" if p.get("notice") else ""
    footer = f"\n\n---\n\n*Source: {source['title']} ({p['url']}). {source['license']}*\n"

    pages = list(range(p["first_page"] - 1, p["last_page"]))
    lines = clean(pymupdf4llm.to_markdown(doc, pages=pages, show_progress=False), strip)

    chapters, part, current, pending = [], None, None, None
    for line in lines:
        if part_re and part_re.search(line):
            pending = "part"
            continue
        if chapter_re.search(line):
            current = {"label": chapter_re.search(line).group(1), "title": None, "part": part, "lines": []}
            chapters.append(current)
            pending = "chapter"
            continue
        text = heading_text(line)
        if pending and text:
            if pending == "part":
                part = text
            else:
                current["title"] = text
            pending = None
            continue
        if current is not None:
            current["lines"].append(line)

    extras = []
    for extra in p.get("extra_pages", []):
        md = pymupdf4llm.to_markdown(doc, pages=list(range(extra["first"] - 1, extra["last"])), show_progress=False)
        extras.append((extra, clean(md, strip)))

    body = [l for ch in chapters for l in ch["lines"] if not HEADING.match(l)]
    body += [l for _, ls in extras for l in ls if not HEADING.match(l)]
    headings = Headings(body, p.get("repair_initials", False))

    for ch in chapters:
        label = ch["label"]
        number = label.split()[-1]
        title = headings.fix(ch["title"] or label)
        part = headings.fix(ch["part"]) if ch["part"] else p["name"]
        fname_title = f"{p['name']} {number.zfill(2) if number.isdigit() else number} - {title}"
        text = headings.render(ch["lines"])
        out.page(fname_title, f"# {label}: {title}\n\n{notice}{text}{footer}", [part])

    for extra, lines in extras:
        text = headings.render(lines)
        out.page(f"{p['name']} - {extra['title']}", f"# {extra['title']}\n\n{text}{footer}",
                 [extra.get("category", p["name"])])

    return p.get("edition", "unknown")
