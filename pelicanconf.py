#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'HELMI'
SITENAME = u'Super HELMI - ICANUX'
SITEURL = 'http://sh.icanux.org'

PATH = 'content'

TIMEZONE = 'America/Lima'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM ='category/%s.atom'
TAG_FEED_ATOM = 'tag/%s.atom'
FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_RSS ='category/%s.rss'
TAG_FEED_RSS = 'tag/%s.rss'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('ICANUX', 'http://icanux.org'),
	 ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/icanux'),
          ('Twitter', 'http://twitter.com/icanux'),
          ('Facebook', 'http://facebook.com/icanux'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'archive/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/{slug}.html'
THEME = "pelican-bootstrap3"

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
