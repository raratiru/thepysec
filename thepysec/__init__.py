#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Fri 31 May 2019 10:28:45 PM EEST (22:28)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (1, 1, 0, "alpha", 2)

__version__ = get_version(VERSION)
