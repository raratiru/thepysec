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