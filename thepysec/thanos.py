#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/thanos.py
#
#       Creation Date : Sun 27 Oct 2019 01:44:22 PM EET (13:44)
#
#       Last Modified : Sun 27 Oct 2019 02:48:53 PM EET (14:48)
#
# ==============================================================================


def get_formset_alive(formset_class, data, instance=None, initial=None):
    """
    https://schinckel.net/2016/04/30/%28directly%29-testing-django-formsets/
    formset = get_formset_alive(MyFormSet, [
        # Form 1
        {
          'foo': ['bar1', 'bar2'],
          'baz': 'qux1',
        },
        # Form 2
        {
          'foo': ['cam1'],
          'baz': 'eggs',
        },
    ])
    ============================================================================
    Many to many field is represented with a list:
        '{}-{}-{}'.format(prefix, form_number, field_name) = ['val_1', 'val_2']
    instead of the original:
        '{}-{}-{}_{}'.format(prefix, form_number, field_name, value_number=1) = 'val_1'
        '{}-{}-{}_{}'.format(prefix, form_number, field_name, value_number=2) = 'val_2'
    ============================================================================
    """
    prefix = formset_class().prefix
    formset_data = {}
    for i, form_data in enumerate(data):
        for name, value in form_data.items():
            formset_data["{}-{}-{}".format(prefix, i, name)] = value
    formset_data["{}-TOTAL_FORMS".format(prefix)] = len(data)
    formset_data["{}-INITIAL_FORMS".format(prefix)] = len(initial) if initial else 0
    if instance:
        return formset_class(formset_data, instance=instance, initial=initial)
    else:
        return formset_class(formset_data, initial=initial)
