#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import reduce
from typing import Any, Union


def deep_getattr(
    obj: Any, string: str, default: Union[str, int, bool]
) -> Union[str, int, bool]:
    """
    Dives in an object by performing successive getattrs for each word in a dotted string.
    It is much faster than using functools.reduce.
    """
    current = obj
    for each in string.split("."):
        current = getattr(current, each, default)
    return current


def deep_get(dictionary: dict, keys: list, default=None):
    """
    Dives in a dictionary by performing successive gets for each word in a dotted string.
    Returns default if the key does not exist.
    """
    return reduce(
        lambda d, key: d.get(key, default) if isinstance(d, dict) else default,
        keys.split("."),
        dictionary,
    )
