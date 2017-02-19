#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')
import commonconf

SITEURL = "https://drummyfish.github.io"
PUBLISH_INFO_TEXT = u'publish version'

commonconf.set_common_variables(sys.modules[__name__])