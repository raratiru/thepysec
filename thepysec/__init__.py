#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Sat 26 Jan 2019 09:55:03 PM EET
#
#       Developer : raratiru  | https://twitter.com/raratiru
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (1, 0, 0, 'alpha', 2)

__version__ = get_version(VERSION)
