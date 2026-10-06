#!/usr/bin/env python3
"""Build content for the sources in sources.json.

  build.py <source-id> <out-dir>   build one source into an empty directory
  build.py --list                  source ids as a JSON array (for CI)
  build.py --readme                regenerate the catalog in README.md
"""

import importlib
import json
import os
import sys

from converters.lib.output import Output

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "https://github.com/Denrox/offline-library"
CATALOG_START = "<!-- catalog:start -->"
CATALOG_END = "<!-- catalog:end -->"


def load_sources():
    with open(os.path.join(HERE, "sources.json"), encoding="utf-8") as f:
        return json.load(f)["sources"]


def build(source_id, out_dir):
    source = next((s for s in load_sources() if s["id"] == source_id), None)
    if not source:
        sys.exit(f"unknown source: {source_id}")
    if os.path.exists(out_dir) and os.listdir(out_dir):
        sys.exit(f"{out_dir} is not empty")
    converter = importlib.import_module(f"converters.{source['converter']}")
    out = Output(out_dir, source)
    snapshot = converter.build(out, source)
    stats = out.finish(snapshot)
    print(f"{source_id}: {stats['pages']} pages, {stats['categories']} categories ({snapshot})")


def readme():
    rows = ["| Topic | Source | Pages from | License | Add to ui-apt-mirror |", "|---|---|---|---|---|"]
    for s in sorted(load_sources(), key=lambda s: (s["topic"], s["title"])):
        url = f"{REPO}/tree/{s['id']}"
        rows.append(f"| {s['topic']} | **{s['title']}** — {s['description']} | {s['source_url']} | {s['license']} | `{url}` |")
    path = os.path.join(HERE, "README.md")
    text = open(path, encoding="utf-8").read()
    start, end = text.index(CATALOG_START) + len(CATALOG_START), text.index(CATALOG_END)
    open(path, "w", encoding="utf-8").write(text[:start] + "\n" + "\n".join(rows) + "\n" + text[end:])


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--list"]:
        print(json.dumps([s["id"] for s in load_sources()]))
    elif args == ["--readme"]:
        readme()
    elif len(args) == 2:
        build(*args)
    else:
        sys.exit(__doc__)
