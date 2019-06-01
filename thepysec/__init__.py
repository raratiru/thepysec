#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Sat 01 Jun 2019 01:14:14 PM EEST (13:14)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (1, 1, 0, "alpha", 3)

__version__ = get_version(VERSION)
