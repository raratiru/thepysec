#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Mon 30 Mar 2020 01:33:58 AM EEST (01:33)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (2, 0, 3, "final", 0)

__version__ = get_version(VERSION)
