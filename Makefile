QUARTO?=quarto
BASE?=origin/main

.PHONY: help preview post changed html publish github clean

help:
	@echo 'Quarto Asterisk blog'
	@echo
	@echo 'Writing (fast):'
	@echo '  make preview              live preview (rebuilds on save)'
	@echo '  make post SLUG=my-slug    render one post + refresh index'
	@echo '  make changed              render posts changed vs working tree / $(BASE)'
	@echo
	@echo 'Publish (slow full site):'
	@echo '  make html                 full quarto render -> _site/'
	@echo '  make github               full render, then publish to gh-pages'
	@echo '  make publish              alias for html'
	@echo
	@echo 'Other:'
	@echo '  make clean                remove _site/ and .quarto/'
	@echo '  BASE=HEAD~1 make changed  choose git base for "changed"'

preview:
	$(QUARTO) preview

# Render a single post directory: posts/$(SLUG)/
post:
ifndef SLUG
	$(error Set SLUG, e.g. make post SLUG=achieve)
endif
	@test -e posts/$(SLUG)/index.qmd -o -e posts/$(SLUG)/index.ipynb \
		|| (echo 'No posts/$(SLUG)/index.qmd or index.ipynb' >&2; exit 1)
	@if [ -f posts/$(SLUG)/index.ipynb ]; then \
		$(QUARTO) render posts/$(SLUG)/index.ipynb; \
	else \
		$(QUARTO) render posts/$(SLUG)/index.qmd; \
	fi
	$(QUARTO) render index.qmd

changed:
	BASE=$(BASE) python3 scripts/render_changed.py --base $(BASE)

html:
	$(QUARTO) render

publish: html

github: html
	$(QUARTO) publish gh-pages --no-prompt --no-render

clean:
	rm -rf _site .quarto
