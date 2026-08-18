# Asterisk blog

Hosted at <https://asterisk.dynevor.org>.

Static site generated with [Quarto](https://quarto.org/) (Pandoc under the hood).

## Setup

Install [Quarto](https://quarto.org/docs/get-started/).

Optional notebook authoring tools: Python, Jupyter, and [Jupytext](https://github.com/mwouts/jupytext).

## Day-to-day writing (fast)

Prefer these over a full-site render:

```bash
make preview                 # live reload while editing
make post SLUG=achieve       # render one post + refresh the listing
make changed                 # render posts changed in git (vs origin/main)
BASE=HEAD~1 make changed     # optional: different git base
```

`execute.freeze: auto` in `_quarto.yml` skips re-running notebook code on full
builds unless the notebook source changed.

## Publish (slow — full site)

```bash
make html       # full quarto render -> _site/
make github     # full render, then publish to gh-pages (--no-render)
```

## Content

- Posts live in `posts/<slug>/index.qmd` (or `index.ipynb`).
- Site config: `_quarto.yml`.
- Citations use `chicago-author-date.csl`. Bibliographies are set only on posts that cite (`bibliography:` in the post YAML), pointing at `blog.bib`, `bible.bib`, and/or `data-science-bib/data_science.bib`.
- Pandoc-style citations work as usual: `@key`, `[@key]`.
- Old Pelican URLs `/{slug}.html` are preserved via Quarto `aliases`.

## Notebook posts

Notebook posts keep stored outputs (`execute: false` in their YAML). Freeze still
applies on project renders. To rebuild from R Markdown sources:

```bash
make -C posts ipynbs
```

Hide code cells with Quarto/`remove-input` cell tags (or `#| echo: false`).

## Migration helpers

```bash
python3 scripts/pelican_to_quarto.py
python3 scripts/port_notebooks.py
python3 scripts/normalize_taxonomy.py   # canonicalize categories / keywords
python3 scripts/render_changed.py       # same as make changed
```
