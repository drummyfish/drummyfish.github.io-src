# -*- coding: utf-8 -*-
#
# Downloads the list of subreddits using browser cookies.
# The reason PRAW is not used is that it requires
# an authentication which leads to saving vulnerable data
# (password, secret) in plain-text files and what not! We
# don't want no authentication.
#
# The final list is saved to template files as subreddits.html.
#
# requires browsercookie (pip install browsercookie)

import requests
import browsercookie
import sys
import time

def get_subreddits(use_cookies):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
  address = "https://www.reddit.com/subreddits"

  if use_cookies:
    cj = browsercookie.firefox()
    html = requests.get(address,cookies=cj,headers=headers).text
  else:
    html = requests.get(address,headers=headers).text
  
  html = html[:html.find("multireddit of")]
  html = html[html.rfind("href="):]
  html = html[html.rfind("/") + 1:html.find(" ") - 1]

  subreddits = html.split("+")
  subreddits = list(map(lambda x: str(unicode(x)), subreddits))
  return subreddits

my_subreddits = get_subreddits(True)
time.sleep(3)                                   # to not look like a bot
default_subreddits = get_subreddits(False)

if set(my_subreddits) == set(default_subreddits):
  print("ERROR: Your subreddits seem to be the same as the default ones! This can't be! Make sure you are logged in reddit with Firefox (its cookies are needed).")
  sys.exit(1)
elif len(my_subreddits) <= 1:
  print("ERROR: No subreddits found! Maybe reddit suspects we're using a bot, wait a few minutes and try again.")
  sys.exit(1)
else:
  print("All seems to be OK, " + str(len(my_subreddits)) + " subreddits found.")

  with open("themes/tastyfish/templates/subreddits.html","w") as template_file:
    template_file.write("{% set subreddits = " + str(my_subreddits) + " %}")
