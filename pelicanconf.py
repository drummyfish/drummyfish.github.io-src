#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')
import commonconf

SITEURL = '/home/tastyfish/Git/drummyfish.github.io'
PUBLISH_INFO_TEXT = u'local version (for testing, you shouldn\'t see this online)'

commonconf.set_common_variables(sys.modules[__name__])