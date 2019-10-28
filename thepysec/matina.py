#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/matina.py
#
#       Creation Date : Mon 28 Oct 2019 06:54:11 PM EET (18:54)
#
#       Last Modified : Mon 28 Oct 2019 06:54:44 PM EET (18:54)
#
# ==============================================================================

from thepysec.lia import pop_wsp


def pop_i18n_wsp(instance, translated_fields):
    """
    In a django model with translated attributes, it strips white space from all
    fields of a translated attribute (attribute_en, attribute_fr, attribute_el).
    """
    for field in translated_fields:
        setattr(instance, field, pop_wsp(getattr(instance, field)))
