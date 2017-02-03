# config both for local and publish

import __builtin__

def set_common_variables(module_ref):
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
  module_ref.DISPLAY_CATEGORIES_ON_MENU = True
  module_ref.DEFAULT_LANG = u'cs'
  module_ref.THEME = "./themes/tastyfish"
  module_ref.PAGE_ORDER_BY = "date"
  module_ref.FEED_ALL_ATOM = "all.rss.xml"
  module_ref.CATEGORY_FEED_ATOM = None
  module_ref.TRANSLATION_FEED_ATOM = None
  module_ref.AUTHOR_FEED_ATOM = None
  module_ref.AUTHOR_FEED_RSS = None
  module_ref.RELATIVE_URLS = True
  module_ref.START_PAGE = "pages/intro.html"
  module_ref.MARKDOWN = {"markdown.extensions.tables" : {}}
