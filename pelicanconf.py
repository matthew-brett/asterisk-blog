#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
from os.path import join as pjoin

AUTHOR = 'Matthew Brett'
AUTHORS = {AUTHOR: 'https://matthew.dynevor.org'}
SITENAME = 'Asterisk'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# The Elegant theme does not use the LINK variable.  I use the
# about.md page for that information.
LINKS =  (
    ('Personal pages', 'http://matthew.dynevor.org'),
    ('Work pages',
     'https://www.birmingham.ac.uk/staff/profiles/psychology/brett-matthew.aspx'),
    ('Nipy', 'http://nipy.org/'),
    ('GitHub', 'https://github.com/matthew-brett'),
    ('atom', '/feeds/all.atom.xml'),
)

# Social widget
SOCIAL = (
    ('rss', '/feeds/all.atom.xml'),
)
SOCIAL_PROFILE_LABEL = 'Atom feed'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra', 'downloads']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'},
    'extra/.htaccess': {'path': '.htaccess'},
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Content caching for faster builds
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'
CONTENT_CACHING_LAYER = 'reader'

sys.path += ['plugins/pelican-plugins',
             'plugins/pelican-plugins/tipue_search/pelican/plugins',
             'plugins/pelican_pandoc_reader/src',
             'plugins/pelican-plugins',
             'plugins/ipynb',
             'plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
    'pelican_pandoc_reader',
]

PANDOC_ARGS = ['--no-highlight',  # use highlight.js instead
               '--section-divs',  # wrap heading-blocks with <section>
               '--citeproc',
               '--bibliography', 'data-science-bib/data_science.bib',
               '--bibliography', 'blog.bib']

SHOW_ARCHIVES = True
ENABLE_MATHJAX = True

# Variables for pelitools
DEFAULT_EXT = 'pdc'
EDIT_CMD = ['gvim', '--remote-silent']

# Ipynb
MARKUP = ['md', 'ipynb']
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_NB_SAVE_AS = '{slug}.ipynb'
# IPYNB_EXPORT_TEMPLATE = 'nbextensions'

sys.path.append(pjoin('plugins', 'ipynb'))
from pelican_jupyter import markup as nb_markup
PLUGINS += [nb_markup]

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

THEME = 'theme/elegant'

# As recommended at
# https://pelican-elegant.github.io/configuration-variables-and-metadata-list
# with modifications from
# https://github.com/Pelican-Elegant/documentation/blob/master/pelicanconf.py
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
STATIC_PATHS.append('theme/images')
PLUGINS += ['sitemap', 'extract_toc', 'tipue_search',
            'neighbors', 'assets', 'share_post']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    }
}
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

# sitemap config
SITEMAP = dict(format='xml')

LIQUID_CONFIGS = (('SITEURL', SITEURL, "The site URL"),)

# Hide cells with hide_input tag
sys.path.append('plugins')
from hideinputs import HideInputs
IPYNB_PREPROCESSORS = [HideInputs]

# Set pandoc markdown flavor
PANDOC_FORMAT_MAP = {'pdc': 'markdown+footnotes'}

# For share_links. All-caps variables available in Jinja2 templates.
# https://docs.getpelican.com/en/stable/themes.html
MY_EMAIL = 'matthew.brett+blog@gmail.com'
COMMENT_BODY = """\
I will append your comment to the post.  Any format is OK, but Markdown works
best for me.
"""

# https://github.com/danielfrg/pelican-jupyter/issues/126#issuecomment-745372454
from pelican_jupyter import liquid as nb_liquid

PLUGINS += [nb_liquid]

# configuring notebook integration
LIQUID_CONFIGS = (("IPYNB_FIX_CSS", "False", ""), 
                  ("IPYNB_SKIP_CSS", "False", ""), 
                  ("IPYNB_EXPORT_TEMPLATE", "base", ""),)
