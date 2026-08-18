#!/usr/bin/env python3
"""Port Pelican notebook posts to Quarto posts/{slug}/index.ipynb."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import as_list, split_taxonomy  # noqa: E402

CONTENT = ROOT / "content"
POSTS = ROOT / "posts"

NOTEBOOKS = [
    "hows-julia",
    "hows-julia-2020",
    "hows-julia-2021",
    "time-to-call-it",
]

FILENAME_LINK = re.compile(r"\]\(\{filename\}/?([^)]+)\)")


def parse_nbdata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8").lstrip("\ufeff \t\r\n")
    # .nbdata is YAML-ish without enclosing ---
    return yaml.safe_load(text) or {}


def frontmatter_from_nbdata(meta: dict, slug: str) -> dict:
    categories, keywords = split_taxonomy(
        categories=as_list(meta.get("Category") or meta.get("Categories")),
        tags=as_list(meta.get("Tags") or meta.get("tags")),
    )
    out = {
        "title": meta.get("Title") or slug,
        "aliases": [f"/{slug}.html"],
        "date": str(meta.get("Date")),
        "categories": categories or None,
        "keywords": keywords or None,
        "description": str(meta.get("Summary") or "").strip() or None,
        "execute": {"enabled": False},
    }
    return {k: v for k, v in out.items() if v is not None}


def dump_yaml(data: dict) -> str:
    return yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True, default_flow_style=False
    )


def rewrite_markdown(text: str) -> str:
    def repl(match: re.Match) -> str:
        stem = Path(match.group(1).strip()).stem
        return f"](/posts/{stem}/)"

    text = FILENAME_LINK.sub(repl, text)
    text = re.sub(r"\]\(\.\./downloads/", "](/downloads/", text)
    text = re.sub(r"\]\(downloads/", "](/downloads/", text)
    text = re.sub(r"\]\(images/", "](/images/", text)
    text = re.sub(r"\]\(\.\./images/", "](/images/", text)
    return text


def rewrite_code(text: str) -> str:
    # execution cwd is posts/{slug}/ when re-enabled
    return re.sub(
        r"pd\.read_csv\('downloads/",
        "pd.read_csv('../../downloads/",
        text,
    )


def port_one(slug: str) -> None:
    nb_path = CONTENT / f"{slug}.ipynb"
    nbdata_path = CONTENT / f"{slug}.nbdata"
    rmd_path = CONTENT / f"{slug}.Rmd"
    if not nb_path.exists() or not nbdata_path.exists():
        raise SystemExit(f"missing sources for {slug}")

    meta = parse_nbdata(nbdata_path)
    slug = str(meta.get("Slug") or slug)
    fm = frontmatter_from_nbdata(meta, slug)

    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    raw_cell = {
        "cell_type": "raw",
        "metadata": {"quarto": {"role": "frontmatter"}},
        "source": [f"---\n{dump_yaml(fm)}---\n"],
    }

    new_cells = [raw_cell]
    for cell in nb["cells"]:
        cell = json.loads(json.dumps(cell))  # deep copy
        src = cell.get("source", [])
        if isinstance(src, list):
            text = "".join(src)
        else:
            text = src

        if cell.get("cell_type") == "markdown":
            text = rewrite_markdown(text)
        elif cell.get("cell_type") == "code":
            text = rewrite_code(text)
            md = cell.setdefault("metadata", {})
            tags = md.get("tags") or []
            if (
                md.get("hide_input")
                or "remove_input" in tags
                or "hide_input" in tags
            ):
                md["echo"] = False
                # Quarto also respects tags: remove-input / hide-input
                tags = [t for t in tags if t not in {"remove_input", "hide_input"}]
                tags.append("remove-input")
                md["tags"] = tags

        if isinstance(src, list):
            # preserve list-of-lines style if original was list
            if text.endswith("\n"):
                lines = text.splitlines(keepends=True)
            else:
                lines = text.splitlines(keepends=True) or [text]
            cell["source"] = lines
        else:
            cell["source"] = text
        new_cells.append(cell)

    nb["cells"] = new_cells
    out_dir = POSTS / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_nb = out_dir / "index.ipynb"
    out_nb.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    if rmd_path.exists():
        rmd = rmd_path.read_text(encoding="utf-8")
        # Replace jupytext header yaml with Quarto-ish title block after first ---
        # Keep Rmd as authoring source alongside notebook.
        rmd = rewrite_markdown(rmd)
        rmd = rewrite_code(rmd)
        # Prepend Quarto frontmatter note via HTML comment for humans
        header = f"<!-- Quarto post slug: {slug}. Prefer editing index.ipynb or sync via jupytext. -->\n"
        (out_dir / f"{slug}.Rmd").write_text(header + rmd, encoding="utf-8")

    print(f"wrote {out_nb.relative_to(ROOT)}")


def main() -> None:
    for slug in NOTEBOOKS:
        port_one(slug)

    makefile = POSTS / "Makefile"
    makefile.write_text(
        """# Rebuild notebooks from Rmd sources (optional authoring path).
# Run from repo root: make -C posts ipynbs

RMD_SOURCES := $(wildcard */*.Rmd)
IPYNBS := $(patsubst %.Rmd,../%.ipynb,$(notdir $(RMD_SOURCES)))

# Prefer converting each posts/<slug>/<slug>.Rmd -> posts/<slug>/index.ipynb
ipynbs:
\t@for d in */; do \\
\t  slug=$$(basename "$$d"); \\
\t  rmd="$$d$$slug.Rmd"; \\
\t  if [ -f "$$rmd" ]; then \\
\t    echo "jupytext $$rmd -> $$d/index.ipynb"; \\
\t    jupytext "$$rmd" --to ipynb -o "$$d/index.ipynb"; \\
\t  fi; \\
\tdone

.PHONY: ipynbs
""",
        encoding="utf-8",
    )
    print(f"wrote {makefile.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
