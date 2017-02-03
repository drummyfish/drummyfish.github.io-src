#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# config both for local and publish

import __builtin__

def set_common_variables(module_ref):
  module_ref.SITENAME = u'tastyfish'
  module_ref.AUTHOR = u'Miloslav \u010c\xed\u017e'

  module_ref.SOCIAL = (
    ('GitHub','https://github.com/drummyfish'),
    ('Facebook','https://www.facebook.com/miloslav.ciz'),
    ('YouTube','https://www.youtube.com/user/drummyfish'),
    ('Deviantart','http://drummyfish.deviantart.com/'),
    ('reddit','https://www.reddit.com/user/drummyfish/'),)

  module_ref.DEFAULT_PAGINATION = 4
  module_ref.PLUGIN_PATHS = ['plugins']
  module_ref.PLUGINS = ['jinja2content']
  module_ref.PATH = 'content'
  module_ref.TIMEZONE = 'Europe/Prague'
  module_ref.DISPLAY_CATEGORIES_ON_MENU = False
  module_ref.DISPLAY_PAGES_ON_MENU = False
  module_ref.MENUITEMS = [
    (u"Úvod","pages/intro.html"),
    (u"Příspěvky","category/posts.html"),
    (u"Clánky","category/articles.html"),
    (u"Projekty","pages/projekty.html"),
    (u"Tagy","tags.html"),
    (u"O mně","pages/about.html")]
  
  module_ref.DEFAULT_LANG = u'cs'
  module_ref.THEME = "./themes/tastyfish"
  module_ref.PAGE_ORDER_BY = "date"
  module_ref.FEED_ALL_ATOM = "all.rss.xml"
  module_ref.CATEGORY_FEED_ATOM = None
  module_ref.TRANSLATION_FEED_ATOM = None
  module_ref.AUTHOR_FEED_ATOM = None
  module_ref.AUTHOR_FEED_RSS = None
  module_ref.RELATIVE_URLS = True
  module_ref.START_PAGE = "pages/intro.html"  # added this, index.html redirects here
  module_ref.MARKDOWN = {"markdown.extensions.tables" : {}}
  module_ref.SUMMARY_MAX_LENGTH = 10
