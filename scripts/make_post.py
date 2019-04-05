#!/usr/bin/env python
""" Make a new blog post given a title
"""

from os.path import join as pjoin, split as psplit, abspath, dirname
import sys
from datetime import datetime as dt
import re

INPUTDIR = abspath(pjoin(dirname(__file__), '..'))

PARAMS = {}
with open(pjoin(INPUTDIR, 'pelicanconf.py'), 'rt') as fobj:
    source = fobj.read()
exec(source, PARAMS)

OUTPUTDIR = pjoin(INPUTDIR, PARAMS['PATH'])


def title2slug(title):
    slug = title.lower()
    slug = re.sub(r'^[\W]', '', slug)
    slug = re.sub(r'[\W]$', '', slug)
    slug = re.sub(r"[';:\"]", '', slug)
    slug = re.sub(r'[\W]', '-', slug)
    return slug


title = sys.argv[1]
ext = sys.argv[2] if len(sys.argv) > 2 else 'pdc'
date = dt.strftime(dt.today(), '%Y-%m-%d %H:%M')
slug = title2slug(title)
post_fname = pjoin(OUTPUTDIR, f'{slug}.{ext}')

contents = f"""---
Title: {title}
Date: {date}
Slug: {slug}
Author: {PARAMS['AUTHOR']}
---


"""

print(f"{post_fname}")
with open(post_fname, 'wt') as fobj:
    fobj.write(contents)
