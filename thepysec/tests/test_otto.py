#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from thepysec import otto


def test_getattr():
    class A:
        a = "John"

    class B:
        b = A()

    assert otto.deep_getattr(B(), "b.a", False) == "John"
    assert otto.deep_getattr(B(), "x.y.z", "George") == "George"


def test_get():
    testing_dict = {"a": 1, "b": {"c": 2}}

    assert otto.deep_get(testing_dict, "b.c", None) == 2
    assert otto.deep_get(testing_dict, "a.c", None) is None
    assert otto.deep_get(testing_dict, "a", None) == 1
