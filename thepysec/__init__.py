#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Mon 08 Apr 2019 06:55:40 PM EEST (18:55)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (1, 1, 1, 'alpha', 1)

__version__ = get_version(VERSION)
