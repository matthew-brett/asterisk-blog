#!/usr/bin/env python3
"""Convert Pelican .pdc posts to Quarto posts/{slug}/index.qmd."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import as_list, split_taxonomy  # noqa: E402

CONTENT = ROOT / "content"
POSTS = ROOT / "posts"

SKIP_NAMES = {"2", "tmp.pdf"}
NOTEBOOK_SLUGS = {
    "hows-julia",
    "hows-julia-2020",
    "hows-julia-2021",
    "time-to-call-it",
}

FILENAME_LINK = re.compile(r"\]\(\{filename\}/?([^)]+)\)")


def parse_pelican(text: str) -> tuple[dict, str]:
    stripped = text.lstrip("\ufeff \t\r\n")
    if not stripped.startswith("---"):
        return {}, text
    parts = stripped.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta = yaml.safe_load(parts[1]) or {}
    body = parts[2].lstrip("\n")
    return meta, body


def slug_from_meta_or_path(meta: dict, path: Path) -> str:
    slug = meta.get("Slug") or meta.get("slug")
    if slug:
        return str(slug).strip()
    return path.stem


def resolve_ref(ref: str, stem_to_slug: dict[str, str]) -> str:
    stem = Path(ref).name
    stem = Path(stem).stem
    return stem_to_slug.get(stem, stem)


def rewrite_body(body: str, stem_to_slug: dict[str, str]) -> str:
    def repl(match: re.Match) -> str:
        slug = resolve_ref(match.group(1).strip(), stem_to_slug)
        return f"](/posts/{slug}/)"

    body = FILENAME_LINK.sub(repl, body)
    body = re.sub(r"\]\(images/", "](/images/", body)
    body = re.sub(r"\]\(\./images/", "](/images/", body)
    body = re.sub(r"\]\(downloads/", "](/downloads/", body)
    return body


def quarto_yaml(meta: dict, slug: str) -> dict:
    title = meta.get("Title") or meta.get("title") or slug
    date = meta.get("Date") or meta.get("date")
    categories, keywords = split_taxonomy(
        categories=as_list(meta.get("Category") or meta.get("Categories")),
        tags=as_list(meta.get("Tags") or meta.get("tags")),
    )

    out: dict = {
        "title": title,
        "aliases": [f"/{slug}.html"],
    }
    if date:
        out["date"] = str(date)
    if categories:
        out["categories"] = categories
    if keywords:
        out["keywords"] = keywords
    author = meta.get("Author") or meta.get("author")
    if author and str(author) != "Matthew Brett":
        out["author"] = str(author)

    status = str(meta.get("Status") or meta.get("status") or "").lower()
    if status in {"draft", "hidden"}:
        out["draft"] = True

    summary = meta.get("Summary") or meta.get("summary")
    if summary:
        out["description"] = str(summary).strip()

    return out


def dump_frontmatter(data: dict) -> str:
    return yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )


def build_stem_to_slug(paths: list[Path]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        meta, _ = parse_pelican(text)
        slug = slug_from_meta_or_path(meta, path)
        mapping[path.stem] = slug
        mapping[slug] = slug
    # notebook stems
    for slug in NOTEBOOK_SLUGS:
        mapping[slug] = slug
    return mapping


def convert_pdc(path: Path, stem_to_slug: dict[str, str]) -> None:
    if path.name in SKIP_NAMES or path.suffix != ".pdc":
        return
    if path.parent.name == "pages":
        return

    text = path.read_text(encoding="utf-8")
    meta, body = parse_pelican(text)
    slug = slug_from_meta_or_path(meta, path)
    if slug in NOTEBOOK_SLUGS:
        print(f"skip notebook-managed slug: {slug} ({path.name})")
        return

    qmeta = quarto_yaml(meta, slug)
    body = rewrite_body(body, stem_to_slug)
    out_dir = POSTS / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.qmd"
    content = f"---\n{dump_frontmatter(qmeta)}---\n\n{body}"
    if not body.endswith("\n"):
        content += "\n"
    out_path.write_text(content, encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)}")


def main() -> None:
    if POSTS.exists():
        shutil.rmtree(POSTS)
    POSTS.mkdir(parents=True)

    paths = sorted(CONTENT.glob("*.pdc"))
    stem_to_slug = build_stem_to_slug(paths)
    for path in paths:
        convert_pdc(path, stem_to_slug)
    print(f"converted {len(list(POSTS.iterdir()))} post directories")


if __name__ == "__main__":
    main()
