#!/usr/bin/env python3
"""Normalize categories/keywords across existing Quarto posts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import as_list, split_taxonomy  # noqa: E402

POSTS = ROOT / "posts"


def dump_frontmatter(data: dict) -> str:
    return yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )


def normalize_meta(meta: dict) -> dict:
    cats, keys = split_taxonomy(
        categories=as_list(meta.get("categories")),
        keywords=as_list(meta.get("keywords")),
        tags=as_list(meta.get("tags")),
    )
    meta = dict(meta)
    meta.pop("tags", None)
    if cats:
        meta["categories"] = cats
    else:
        meta.pop("categories", None)
    if keys:
        meta["keywords"] = keys
    else:
        meta.pop("keywords", None)
    return meta


def normalize_qmd(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    meta = yaml.safe_load(parts[1]) or {}
    new_meta = normalize_meta(meta)
    if new_meta == meta:
        return False
    body = parts[2]
    path.write_text(
        f"---\n{dump_frontmatter(new_meta)}---{body}",
        encoding="utf-8",
    )
    return True


def normalize_ipynb(path: Path) -> bool:
    nb = json.loads(path.read_text(encoding="utf-8"))
    if not nb.get("cells"):
        return False
    cell = nb["cells"][0]
    if cell.get("cell_type") != "raw":
        return False
    src = cell.get("source", [])
    text = "".join(src) if isinstance(src, list) else src
    if "---" not in text:
        return False
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    meta = yaml.safe_load(parts[1]) or {}
    new_meta = normalize_meta(meta)
    if new_meta == meta:
        return False
    new_src = f"---\n{dump_frontmatter(new_meta)}---\n"
    cell["source"] = [new_src]
    path.write_text(
        json.dumps(nb, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return True


def main() -> None:
    changed = 0
    for path in sorted(POSTS.glob("*/index.qmd")):
        if normalize_qmd(path):
            print(f"updated {path.relative_to(ROOT)}")
            changed += 1
    for path in sorted(POSTS.glob("*/index.ipynb")):
        if normalize_ipynb(path):
            print(f"updated {path.relative_to(ROOT)}")
            changed += 1
    print(f"changed {changed} posts")


if __name__ == "__main__":
    main()
