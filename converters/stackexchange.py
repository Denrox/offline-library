"""A Stack Exchange site from its Kiwix ZIM file: the well-received questions,
each with its best answers, grouped into categories by tag.

A question is kept when its score is at least min_question_score and it has an
accepted answer or one scoring at least min_answer_score. Its page holds the
question and up to max_answers answers: the accepted one first, then the rest
by score, each scoring at least min_answer_score. Comments, user pages and
images are left out. Every page names its authors and links to the original,
as CC BY-SA requires.

Params (sources.json):
  zim                 URL of the site's .zim file (download.kiwix.org)
  site_url            the live site, e.g. "https://ham.stackexchange.com"
  min_question_score, min_answer_score, max_answers
  tag_categories      [["Category", ["tag", "tag-prefix*", ...]], ...]; a question
                      goes to every category one of its tags is in, or to
                      other_category when none is
  other_category      category for questions no listed tag covers
"""

import html
import os
import re
import tempfile
import time
import urllib.parse
import urllib.request

from .lib.html2md import html_to_md

UA = "offline-library (https://github.com/Denrox/offline-library)"


def download(url, path, attempts=4):
    for attempt in range(1, attempts + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
                while chunk := r.read(1 << 20):
                    f.write(chunk)
            return
        except OSError:
            if attempt == attempts:
                raise
            time.sleep(15 * attempt)


def inner_div(page, start):
    """The HTML inside the <div> that opens at `start`."""
    open_end = page.index(">", start) + 1
    depth, i = 1, open_end
    for m in re.finditer(r"<(/?)div\b", page[open_end:]):
        depth += -1 if m[1] else 1
        if depth == 0:
            return page[open_end:open_end + m.start()]
        i = open_end + m.end()
    return page[open_end:i]


def post(segment, verb):
    """(score, body html, author) of the question or answer in `segment`."""
    score = int(re.search(r'data-score="(-?\d+)"', segment)[1])
    body = inner_div(segment, segment.index('<div class="s-prose js-post-body"'))
    m = re.search(r'datetime="' + verb + r'[^"]*".*?class="s-user-card--link">([^<]+)<', segment, re.S)
    return score, body, html.unescape(m[1].strip()) if m else None


def categories_for(tags, tag_categories, other):
    out = []
    for category, patterns in tag_categories:
        if any(t == p or (p.endswith("*") and t.startswith(p[:-1])) for t in tags for p in patterns):
            out.append(category)
    return out or [other]


def build(out, source):
    from libzim.reader import Archive  # only this converter needs libzim

    p = source["params"]
    site = p["site_url"].rstrip("/")
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "site.zim")
        download(p["zim"], path)
        z = Archive(path)
        for i in range(z.entry_count):
            e = z._get_entry_by_id(i)
            if e.is_redirect or not re.fullmatch(r"questions/\d+/[^/]+", e.path):
                continue
            page = bytes(e.get_item().content).decode("utf-8")
            # Links inside the site: make them absolute, so links between kept questions survive.
            # Links inside the site (the ZIM writes them as "//:None/../../a/1009"): absolute again,
            # so links between kept questions and to their answers survive.
            here = f"{site}/{e.path}"
            page = re.sub(r'href="(?://:None/)?(?![a-z]+:|#|//)([^"]*)"',
                          lambda m: f'href="{urllib.parse.urljoin(here, m[1])}"', page)
            parts = re.split(r'(?=<div id="answer-\d+")', page)
            question, answers = parts[0], parts[1:]
            q_score, q_body, asker = post(question[question.index('id="question"'):], "asked")
            if q_score < p["min_question_score"]:
                continue

            kept = []
            for a in answers:
                score, body, author = post(a, "answered")
                accepted = 'itemprop="acceptedAnswer"' in a[:600]
                if accepted or score >= p["min_answer_score"]:
                    kept.append((not accepted, -score, score, accepted, body, author))
            if not kept:
                continue
            kept = sorted(kept)[:p["max_answers"]]

            title = html.unescape(re.search(r'class="question-hyperlink">([^<]+)<', question)[1]).strip()
            tags = re.findall(r'rel="tag">([^<]+)<', question)
            qid = e.path.split("/")[1]
            url = f"{site}/{e.path}"
            md = [f"# {title}\n", f"*Tags: {', '.join(tags)} · score {q_score}*\n", "## Question\n",
                  html_to_md(q_body, site)]
            for _, _, score, accepted, body, author in kept:
                md += [f"## {'Accepted answer' if accepted else 'Answer'} (score {score}{f', by {author}' if author else ''})\n",
                       html_to_md(body, site)]
            people = ", ".join(dict.fromkeys(x for x in [asker] + [k[5] for k in kept] if x))
            md.append(f"---\n\n*Source: {source['title']}, {url}, by {people}. {source['license']}*\n")
            answer_ids = re.findall(r'<div id="answer-(\d+)"', page)
            urls = [url, f"{site}/questions/{qid}", f"{site}/q/{qid}"] + [f"{site}/a/{a}" for a in answer_ids]
            out.page(title, "\n".join(md), categories_for(tags, p["tag_categories"], p["other_category"]), urls=urls)
    return re.search(r"_(\d{4}-\d{2})\.zim$", p["zim"])[1]
