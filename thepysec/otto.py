#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
