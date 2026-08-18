# Rebuild notebooks from Rmd sources (optional authoring path).
# Run from repo root: make -C posts ipynbs

RMD_SOURCES := $(wildcard */*.Rmd)
IPYNBS := $(patsubst %.Rmd,../%.ipynb,$(notdir $(RMD_SOURCES)))

# Prefer converting each posts/<slug>/<slug>.Rmd -> posts/<slug>/index.ipynb
ipynbs:
	@for d in */; do \
	  slug=$$(basename "$$d"); \
	  rmd="$$d$$slug.Rmd"; \
	  if [ -f "$$rmd" ]; then \
	    echo "jupytext $$rmd -> $$d/index.ipynb"; \
	    jupytext "$$rmd" --to ipynb -o "$$d/index.ipynb"; \
	  fi; \
	done

.PHONY: ipynbs
