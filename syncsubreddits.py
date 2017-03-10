# -*- coding: utf-8 -*-
#
# Downloads the list of subreddits using browser cookies.
# The reason PRAW is not used is that it requires a
# an authentication which leads to saving vulnerable data
# (password, secret) in plain files and what not! We don't
# want no authentication.
#
# The final list is saved to template files as subreddits.html.
#
# requires browsercookie (pip install browsercookie)

import requests
import browsercookie
import sys

cj = browsercookie.firefox()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
html = requests.get("https://www.reddit.com/subreddits",cookies=cj,headers=headers).text

html = html[:html.find("multireddit of")]
html = html[html.rfind("href="):]
html = html[html.rfind("/") + 1:html.find(" ") - 1]

subreddits = html.split("+")

subreddits = list(map(lambda x: str(unicode(x)), subreddits))

if len(subreddits) <= 1:
  print("No subreddits found!")
  sys.exit(1)
else:
  with open("themes/tastyfish/templates/subreddits.html","w") as template_file:
    template_file.write("{% set subreddits = " + str(subreddits) + " %}")
