#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# config both for local and publish

import __builtin__

def set_common_variables(module_ref):
  module_ref.SITENAME = u"tastyfish"
  module_ref.AUTHOR = u"Miloslav Číž"

  module_ref.OUTPUT_RETENTION = [".hg", ".git", ".bzr"]
  module_ref.DELETE_OUTPUT_DIRECTORY = True

  module_ref.SOCIAL = (
    ("GitHub","https://github.com/drummyfish"),
    ("Facebook","https://www.facebook.com/miloslav.ciz"),
    ("YouTube","https://www.youtube.com/user/drummyfish"),
    ("Deviantart","http://drummyfish.deviantart.com/"),
    ("reddit","https://www.reddit.com/user/drummyfish/"),
    )

  module_ref.DEFAULT_PAGINATION = 4
  module_ref.PLUGIN_PATHS = ["plugins"]
  module_ref.PLUGINS = ["jinja2content","i18n_subsites","pelican_githubprojects"]
  module_ref.GITHUB_USER = "drummyfish"
  module_ref.PATH = 'content'
  module_ref.TIMEZONE = 'Europe/Prague'
  module_ref.DISPLAY_CATEGORIES_ON_MENU = False
  module_ref.DISPLAY_PAGES_ON_MENU = False
  module_ref.MENUITEMS = [
    (u"Úvod","index.html"),
    (u"Příspěvky","category/posts.html"),
    (u"Články","category/articles.html"),
    (u"Projekty","pages/projekty.html"),
    (u"Tagy","tags.html"),
    (u"O mně","pages/about.html")]
  
  module_ref.MENUITEM_ACTIVE_MAPPING = {   # I added this, maps categories to menu item
    "Articles" : 3,                        # indices that should be marked active
    "Posts" : 2,
    "tag" : 5
    }
  
  module_ref.JINJA_ENVIRONMENT = {
    "trim_blocks": True,
    "lstrip_blocks": True
    }
  
  module_ref.DEFAULT_LANG = u'cs'
  module_ref.THEME = "./themes/tastyfish"
  module_ref.PAGE_ORDER_BY = "date"
  module_ref.FEED_ALL_ATOM = "all.rss.xml"
  module_ref.CATEGORY_FEED_ATOM = None
  module_ref.TRANSLATION_FEED_ATOM = None
  module_ref.AUTHOR_FEED_ATOM = None
  module_ref.AUTHOR_FEED_RSS = None
  module_ref.RELATIVE_URLS = False
  module_ref.START_PAGE = "pages/intro.html"  # added this, index.html redirects here
  module_ref.MARKDOWN = {
      "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.tables" : {}
    },
    "output_format": "html5",
    }
  module_ref.SUMMARY_MAX_LENGTH = 30
  module_ref.I18N_SUBSITES = {
    "en": { "MENUITEMS" : [
         (u"Intro","index.html"),
         (u"Posts","category/posts.html"),
         (u"Articles","category/articles.html"),
         (u"Projects","pages/projekty.html"),
         (u"Tags","tags.html"),
         (u"About me","pages/about.html")]
        }
    }
  module_ref.I18N_UNTRANSLATED_ARTICLES = "keep"

  module_ref.STATIC_PATHS = ["images","extra/favicon.ico","../README.md"]
  module_ref.EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "../README.md": {"path": "README.md"}
    }