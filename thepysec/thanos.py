#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/thanos.py
#
#       Creation Date : Sun 27 Oct 2019 01:44:22 PM EET (13:44)
#
#       Last Modified : Mon 28 Oct 2019 06:37:22 PM EET (18:37)
#
# ==============================================================================


def get_formset_alive(formset_class, data, instance=None, initial=None):
    """
    https://schinckel.net/2016/04/30/%28directly%29-testing-django-formsets/
    formset = get_formset_alive(MyFormSet, [
        # Form 1
        {
          'foo': ['bar1', 'bar2'],
          'multi_val': {0: 'val1', 1: 'val2'},
          'baz': 'qux1',
        },
        # Form 2
        {
          'foo': ['cam1'],
          'multi_val': {0: 'zoo1', 1: 'zoo2'},
          'baz': 'eggs',
        },
    ])
    ============================================================================
    Many to many field is represented with a list:
        '{}-{}-{}'.format(prefix, form_number, field_name) = ['val_1', 'val_2']
    Multivalue field is represented with a dict:
    '{}-{}-{}_{}'.format(prefix, form_number, field_name, value_number=key) = value
    ============================================================================
    """
    prefix = formset_class().prefix
    formset_data = {}
    for i, form_data in enumerate(data):
        for name, value in form_data.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    formset_data["{}-{}-{}_{}".format(prefix, i, name, k)] = v
            else:
                formset_data["{}-{}-{}".format(prefix, i, name)] = value
    formset_data["{}-TOTAL_FORMS".format(prefix)] = len(data)
    formset_data["{}-INITIAL_FORMS".format(prefix)] = len(initial) if initial else 0
    if instance:
        return formset_class(formset_data, instance=instance, initial=initial)
    else:
        return formset_class(formset_data, initial=initial)
