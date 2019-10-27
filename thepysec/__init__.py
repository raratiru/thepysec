#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/__init__.py
#
#       Creation Date : Fri 28 Dec 2018 03:36:03 PM EET
#
#       Last Modified : Mon 28 Oct 2019 12:18:14 AM EET (00:18)
#
# ==============================================================================

from thepysec.john.version import get_version


VERSION = (2, 0, 0, "final", 0)

__version__ = get_version(VERSION)
