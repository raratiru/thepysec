#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/lia/tests/test_lia.py
#
#       Creation Date : Sat 16 Mar 2019 03:19:11 PM EET (15:19)
#
#       Last Modified : Mon 28 Oct 2019 12:14:53 AM EET (00:14)
#
# ==============================================================================

from thepysec import lia


def test_pop_whitespace():
    obj = lia.pop_wsp("dadd     d    r")
    assert obj == "dadd d r"


def test_django_pop_whitespace():
    class A:
        att1_en = "f        r                     a"
        att1_fr = "h            b            k"
        att1_el = "h     f       b   y         k"
        att2_en = "r       r                     a"
        att2_fr = "h            f            k"
        att2_el = "h     f       b   1         k"

    obj = A()
    trans_fields = ("att1_en", "att1_el", "att1_fr", "att2_en", "att2_el", "att2_fr")
    lia.pop_i18n_wsp(obj, trans_fields)
    assert all(
        (
            obj.att1_en == "f r a",
            obj.att1_fr == "h b k",
            obj.att1_el == "h f b y k",
            obj.att2_en == "r r a",
            obj.att2_fr == "h f k",
            obj.att2_el == "h f b 1 k",
        )
    )


def test_pre_slug():
    raw_slug = "tr4e, 5435 (bili#go)"
    assert lia.pre_slug(raw_slug) == "tr 4 e 5435 bili go"


def test_fast_pre_slug():
    raw_slug = "tr4e, 5435 (bili#go)"
    assert lia.fast_pre_slug(raw_slug) == "tr 4 e 5 4 3 5 bili go"
