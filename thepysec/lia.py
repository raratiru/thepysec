#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/lia/strings.py
#
#       Creation Date : Sat 16 Mar 2019 03:12:18 PM EET (15:12)
#
#       Last Modified : Sat 01 Jun 2019 01:51:28 PM EEST (13:51)
#
# ==============================================================================

import re
from itertools import product
from unidecode import unidecode


def pop_wsp(lia_string):
    return " ".join(lia_string.split())


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


def fast_pre_slug(lia_string):
    """
    * Decode string to ASCII
    * Lower case for all letters
    * Replace punctuation with space (punctuation in a valid input, has semantic meaning)
    * Add space around numbers
    * Remove extra spaces
    8μs from: 'tr4e, 5435 (bili#go)' to 'tr 4 e 5 4 3 5 bili go'
    pros: Fast, replaces punctuation with space.
    Con: Adds space around all digits
    """
    punctuation = {
        "!": " ",
        '"': " ",
        "#": " ",
        "$": " ",
        "%": " ",
        "&": " ",
        "'": " ",
        "(": " ",
        ")": " ",
        "*": " ",
        "+": " ",
        ",": " ",
        "-": " ",
        ".": " ",
        "/": " ",
        ":": " ",
        ";": " ",
        "<": " ",
        "=": " ",
        ">": " ",
        "?": " ",
        "@": " ",
        "[": " ",
        "\\": " ",
        "]": " ",
        "^": " ",
        "_": " ",
        "`": " ",
        "{": " ",
        "|": " ",
        "}": " ",
        "~": " ",
    }
    numbers = {
        "0": " 0 ",
        "1": " 1 ",
        "2": " 2 ",
        "3": " 3 ",
        "4": " 4 ",
        "5": " 5 ",
        "6": " 6 ",
        "7": " 7 ",
        "8": " 8 ",
        "9": " 9 ",
    }
    return " ".join(
        unidecode(lia_string.lower())
        .translate(str.maketrans({**punctuation, **numbers}))
        .split()
    )


def pre_slug(s):
    """
    * Decode string to ASCII
    * Lower case for all letters
    * Replace punctuation with a space (punctuation in a valid input, has semantic meaning)
    * Add space between numbers and letters
    * Remove extra spaces
    13.5μs from: 'tr4e, 5435 (bili#go)' to 'tr 4 e 5435 biligo'
    pros: Keeps numbers together adding space only between numbers and letters.
    cons: Almost double the time of fast_pre_slug, no space between punctuation and letters.
    """
    punctuation = {
        "!": " ",
        '"': " ",
        "#": " ",
        "$": " ",
        "%": " ",
        "&": " ",
        "'": " ",
        "(": " ",
        ")": " ",
        "*": " ",
        "+": " ",
        ",": " ",
        "-": " ",
        ".": " ",
        "/": " ",
        ":": " ",
        ";": " ",
        "<": " ",
        "=": " ",
        ">": " ",
        "?": " ",
        "@": " ",
        "[": " ",
        "\\": " ",
        "]": " ",
        "^": " ",
        "_": " ",
        "`": " ",
        "{": " ",
        "|": " ",
        "}": " ",
        "~": " ",
    }
    return " ".join(
        re.sub(
            r"([0-9]+(\.[0-9]+)?)",
            r" \1 ",
            unidecode(s.translate(str.maketrans(punctuation)).lower()),
        ).split()
    )
