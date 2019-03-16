#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Sat 16 Mar 2019 04:07:11 PM EET (16:07)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (1, 1, 0, 'alpha', 1)

__version__ = get_version(VERSION)
