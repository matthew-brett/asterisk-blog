#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matthew Brett'
SITENAME = 'Asterisk'
SITEURL = ''

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
LINKS =  (
    ('Personal pages', 'http://matthew.dynevor.org'),
    ('Work pages',
     'https://www.birmingham.ac.uk/staff/profiles/psychology/brett-matthew.aspx'),
    ('Nipy', 'http://nipy.org/'),
    ('GitHub', 'https://github.com/matthew-brett'),
)

# Social widget
SOCIAL = (())

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

PLUGIN_PATHS = ['plugins/pelican_pandoc_reader',
                'plugins/pelican-plugins',
                'plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
    'pelican_pandoc_reader',
    'ipynb.markup'
]

PANDOC_ARGS = ['--no-highlight',  # use highlight.js instead
               '--section-divs',  # wrap heading-blocks with <section>
               '--filter', 'pandoc-citeproc']

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
STATIC_PATHS.append('theme/elegant/images')
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

# License
SITE_LICENSE = """These pages licensed with the <a rel="license"
    href="http://creativecommons.org/licenses/by/4.0/">
    Creative Commons Attribution 4.0 International License</a>."""

# sitemap config
SITEMAP = dict(format='xml')
