#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Sat 26 Oct 2019 09:28:35 PM EEST (21:28)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (1, 1, 0, "alpha", 4)

__version__ = get_version(VERSION)
