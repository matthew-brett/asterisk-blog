
IPYNBS:=$(patsubst %.Rmd,%.ipynb,$(wildcard *.Rmd))

ipynbs: $(IPYNBS)

%.ipynb: %.Rmd
	jupytext $< --execute --to ipynb
