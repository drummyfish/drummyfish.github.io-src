#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')

AUTHOR = u'Miloslav \u010c\xed\u017e'
SITENAME = u'tastyfish'
SITEURL = ''

PLUGIN_PATHS = ['plugins']
PLUGINS = ['jinja2content']

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = u'cs'

THEME = "./themes/tastyfish"

PAGE_ORDER_BY = "date"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "all.rss.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/drummyfish'),
          ('Facebook', 'https://www.facebook.com/miloslav.ciz'),
          ('YouTube', 'https://www.youtube.com/user/drummyfish'),
          ('Deviantart', 'http://drummyfish.deviantart.com/'),
          ('reddit', 'https://www.reddit.com/user/drummyfish/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
