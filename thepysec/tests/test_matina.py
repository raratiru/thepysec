#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/tests/test_matina.py
#
#       Creation Date : Mon 28 Oct 2019 06:55:14 PM EET (18:55)
#
#       Last Modified : Mon 28 Oct 2019 06:56:05 PM EET (18:56)
#
# ==============================================================================

from thepysec import matina


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
    matina.pop_i18n_wsp(obj, trans_fields)
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
