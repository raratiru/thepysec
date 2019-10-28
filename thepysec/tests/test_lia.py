#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/lia/tests/test_lia.py
#
#       Creation Date : Sat 16 Mar 2019 03:19:11 PM EET (15:19)
#
#       Last Modified : Mon 28 Oct 2019 06:56:13 PM EET (18:56)
#
# ==============================================================================

from thepysec import lia


def test_pop_whitespace():
    obj = lia.pop_wsp("dadd     d    r")
    assert obj == "dadd d r"


def test_pre_slug():
    raw_slug = "tr4e, 5435 (bili#go)"
    assert lia.pre_slug(raw_slug) == "tr 4 e 5435 bili go"


def test_fast_pre_slug():
    raw_slug = "tr4e, 5435 (bili#go)"
    assert lia.fast_pre_slug(raw_slug) == "tr 4 e 5 4 3 5 bili go"
