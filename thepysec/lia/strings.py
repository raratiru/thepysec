#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/lia/strings.py
#
#       Creation Date : Sat 16 Mar 2019 03:12:18 PM EET (15:12)
#
#       Last Modified : Fri 31 May 2019 10:22:42 PM EEST (22:22)
#
# ==============================================================================

import string
from itertools import product, repeat
from unidecode import unidecode


def pop_wsp(string):
    return " ".join(string.split())


def pop_i18n_wsp(instance, translated_fields, available_languages):
    """
    In a django model with translated attributes, it strips white space from all
    fields of a translated attribute (attribute_en, attribute_fr, attribute_el).
    """
    for field, language in product(translated_fields, available_languages):
        setattr(
            instance,
            f"{field}_{language}",  # noqa
            pop_wsp(getattr(instance, f"{field}_{language}")),
        )


def pre_slug(lia_string):
    punctuation = dict(zip(list(string.punctuation), repeat(" ")))
    numbers = dict([(str(each), " {0} ".format(each)) for each in string.digits])
    return " ".join(
        unidecode(lia_string.lower())
        .translate(str.maketrans({**punctuation, **numbers}))
        .split()
    )
