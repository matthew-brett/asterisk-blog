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

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.ico': {'path': 'favicon.png'},
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Content caching for faster builds
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'
CONTENT_CACHING_LAYER = 'reader'

PLUGIN_PATHS = ['plugins/pelican_pandoc_reader']
PLUGINS = ['pelican_pandoc_reader']
PANDOC_ARGS = ['--no-highlight',  # use highlight.js instead
               '--section-divs',  # wrap heading-blocks with <section>
               '--filter', 'pandoc-citeproc']
