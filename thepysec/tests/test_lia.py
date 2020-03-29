#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/lia/tests/test_lia.py
#
#       Creation Date : Sat 16 Mar 2019 03:19:11 PM EET (15:19)
#
#       Last Modified : Mon 30 Mar 2020 01:23:25 AM EEST (01:23)
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


def test_cap_sentence():
    sentence = "O'Connor is    INVITED to UK shortly after our friend's birthday"
    assert lia.cap_sentence(sentence) == (
        "O'Connor Is Invited To UK Shortly After Our Friend's Birthday"
    )
