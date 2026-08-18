#!/usr/bin/env python3
"""Render only Quarto inputs changed in the working tree (and vs BASE).

Usage:
  python3 scripts/render_changed.py
  BASE=origin/main python3 scripts/render_changed.py
  python3 scripts/render_changed.py --base HEAD~1
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

GLOBAL_TRIGGERS = {
    "_quarto.yml",
    "styles.css",
    "chicago-author-date.csl",
    "blog.bib",
    "bible.bib",
    "CNAME",
    "favicon.ico",
    "favicon.png",
    "robots.txt",
}

DRAFT_SLUGS: set[str] = set()  # drafts render under draft-mode: unlinked


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=check)


def git_names(*args: str) -> set[str]:
    proc = run(["git", "diff", "--name-only", "--diff-filter=ACMR", *args], check=False)
    if proc.returncode != 0:
        return set()
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}


def changed_paths(base: str | None) -> set[str]:
    names: set[str] = set()
    names |= git_names()  # unstaged
    names |= git_names("--cached")  # staged
    # Untracked Quarto inputs only (ignore other untracked noise)
    proc = run(
        ["git", "ls-files", "--others", "--exclude-standard"],
        check=False,
    )
    if proc.returncode == 0:
        for line in proc.stdout.splitlines():
            rel = line.strip()
            if not rel:
                continue
            path = Path(rel)
            if rel in GLOBAL_TRIGGERS or rel.startswith("data-science-bib/"):
                names.add(rel)
            elif path.name in {"index.qmd", "index.ipynb"} and len(path.parts) == 3 and path.parts[0] == "posts":
                names.add(rel)
            elif path.name in {"index.qmd", "about.qmd"} and len(path.parts) == 1:
                names.add(rel)
    if base:
        probe = run(["git", "rev-parse", "--verify", base], check=False)
        if probe.returncode == 0:
            names |= git_names(f"{base}...HEAD")
    return names


def needs_full_render(paths: set[str]) -> bool:
    for p in paths:
        if p in GLOBAL_TRIGGERS:
            return True
        if p.startswith("data-science-bib/") and p.endswith(".bib"):
            return True
        if p.startswith("images/") or p.startswith("downloads/"):
            return True
        if p.startswith("scripts/taxonomy"):
            return True
    return False


def post_inputs(paths: set[str]) -> list[Path]:
    inputs: set[Path] = set()
    for rel in paths:
        path = Path(rel)
        if path.name in {"index.qmd", "index.ipynb"} and path.parent.parent.name == "posts":
            slug = path.parent.name
            if slug in DRAFT_SLUGS:
                continue
            inputs.add(path)
        elif path.name in {"index.qmd", "about.qmd"} and path.parent == Path("."):
            inputs.add(path)
    # Prefer qmd over listing later; keep stable order
    return sorted(inputs)


def render_one(path: Path) -> None:
    print(f"quarto render {path}")
    subprocess.run(["quarto", "render", str(path)], cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base",
        default=os.environ.get("BASE", "origin/main"),
        help="git ref for committed changes (empty to skip). Default: origin/main",
    )
    parser.add_argument(
        "--full-on-global",
        action="store_true",
        default=True,
        help="fall back to full site render if global config/assets changed",
    )
    args = parser.parse_args()
    base = args.base or None

    paths = changed_paths(base)
    if not paths:
        print("No changed Quarto inputs detected.")
        return 0

    print("Changed paths:")
    for p in sorted(paths):
        print(f"  {p}")

    if args.full_on_global and needs_full_render(paths):
        print("Global config/asset change detected — running full quarto render.")
        subprocess.run(["quarto", "render"], cwd=ROOT, check=True)
        return 0

    inputs = post_inputs(paths)
    if not inputs:
        print("No post/page inputs to render (only non-content changes).")
        return 0

    post_count = sum(1 for p in inputs if p.parts[:1] == ("posts",))
    if post_count > 20:
        print(
            f"{post_count} posts changed — falling back to full quarto render "
            "(use make post SLUG=... for a single post)."
        )
        subprocess.run(["quarto", "render"], cwd=ROOT, check=True)
        return 0

    for path in inputs:
        render_one(path)

    # Refresh listing/feed if any post changed
    if any(p.parts[:1] == ("posts",) for p in inputs):
        if Path("index.qmd") not in inputs:
            render_one(Path("index.qmd"))

    print("Incremental render complete.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(exc.returncode)
