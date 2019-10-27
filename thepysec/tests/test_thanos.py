#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/tests/test_thanos.py
#
#       Creation Date : Sun 27 Oct 2019 02:17:45 PM EET (14:17)
#
#       Last Modified : Sun 27 Oct 2019 02:47:43 PM EET (14:47)
#
# ==============================================================================

from thepysec import thanos


class Inst:
    pass


class MyFormset:
    def __init__(self, data=None, initial=None, instance=None):
        self.data = data
        self.initial = initial
        self.instance = instance
        self.prefix = "myformset"


data = [
    {
        "field1": ["value11", "value12", "value13"],
        "field2": "A value",
        "field3": ["my_val1"],
    },
    {
        "field1": ["value21", "value22", "value23"],
        "field2": "Another value",
        "field3": ["my_val2"],
    },
    {
        "field1": ["value31", "value32", "value33"],
        "field2": "A third value",
        "field3": ["my_val3"],
    },
]

initial = [
    {
        "field1": ["value11", "value12", "value13"],
        "field2": "A value",
        "field3": ["my_val1"],
    }
]


def test_alive_formset():
    formset = thanos.get_formset_alive(MyFormset, data, initial=initial)
    assert formset.data == {
        "myformset-0-field1": ["value11", "value12", "value13"],
        "myformset-0-field2": "A value",
        "myformset-0-field3": ["my_val1"],
        "myformset-1-field1": ["value21", "value22", "value23"],
        "myformset-1-field2": "Another value",
        "myformset-1-field3": ["my_val2"],
        "myformset-2-field1": ["value31", "value32", "value33"],
        "myformset-2-field2": "A third value",
        "myformset-2-field3": ["my_val3"],
        "myformset-TOTAL_FORMS": 3,
        "myformset-INITIAL_FORMS": 1,
    }
    assert formset.initial == initial


def test_alive_formset_instance():
    formset = thanos.get_formset_alive(
        MyFormset, data, instance=Inst(), initial=initial
    )
    assert isinstance(formset.instance, Inst) is True
