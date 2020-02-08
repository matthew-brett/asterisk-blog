# Asterisk blog content

Hosted at <http://asterisk.dynevor.org>.

## Pandoc markdown format for posts

See `requirements.txt` and `pelicanconf.py`.  In `pelicanconf.py`:

```python
# Set Pandoc markdown flavor
sys.path.append(pjoin('plugins', 'pelican_pandoc_reader'))
import pelican_pandoc_reader as pdr
pdr.pandoc_fmt_map['pdc'] = 'markdown+footnotes'
```

## Notebook blogging

I'm using the `ipynb.liquid` plugin for embedding notebooks.

I used RMarkdown for editing notebook blog posts, via the excellent
[Jupytext](https://github.com/mwouts/jupytext).

To allow cell input hiding in RMarkdown notebooks, use `use_runtools: true` in
the `jupytext` section of the notebook metadata, and `echo=FALSE` in the cell
header, as in:

~~~
```{python echo=FALSE}
# Don't show the code for this cell.
```
~~~

See also this configuration snippet in `pelicanconf.py`:

```{python}
# Hide cells with hide_input tag
sys.path.append('plugins')
from hideinputs import HideInputs
IPYNB_PREPROCESSORS = [HideInputs]
```


Set the Pelican metadata such as Category and Title in a matching `.nbdata`
file.

There is an example in `contents/hows-julia-2020.Rmd` and its associated files.
