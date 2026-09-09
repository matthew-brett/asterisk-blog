#!/usr/bin/env python3
"""Copy the Quarto listing feed to legacy Pelican feed URLs."""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

# Historical Pelican paths under /feeds/ (see pre-Quarto site).
LEGACY_FEED_FILES = (
    "all.atom.xml",
    "matthew-brett.atom.xml",
    "matthew-brett.rss.xml",
    "bible-criticism.atom.xml",
    "coding.atom.xml",
    "data-science.atom.xml",
    "g-archive.atom.xml",
    "information.atom.xml",
    "management.atom.xml",
    "misc.atom.xml",
    "nt-criticism.atom.xml",
    "organizations.atom.xml",
    "politics.atom.xml",
    "teaching.atom.xml",
)


def main() -> int:
    out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
    src = out / "index.xml"
    if not src.is_file():
        print(f"copy-legacy-feeds: skip (no {src})", file=sys.stderr)
        return 0

    feeds_dir = out / "feeds"
    feeds_dir.mkdir(parents=True, exist_ok=True)
    for name in LEGACY_FEED_FILES:
        dest = feeds_dir / name
        shutil.copyfile(src, dest)
        print(f"copy-legacy-feeds: {src} -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
