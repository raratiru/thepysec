#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Mon 28 Oct 2019 06:44:46 PM EET (18:44)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (2, 0, 1, "final", 0)

__version__ = get_version(VERSION)
