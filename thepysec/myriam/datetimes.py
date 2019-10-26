#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/myriam/datetimes.py
#
#       Creation Date : Sat 26 Oct 2019 08:48:19 PM EEST (20:48)
#
#       Last Modified : Sat 26 Oct 2019 09:18:24 PM EEST (21:18)
#
# ==============================================================================


def validate_overlap(periods, datetime_range=False):
    """
    Receives a list with DateRange or DateTimeRange and returns True
    if periods overlap.
    This method considers that the end of each period is not inclusive:
    If a period ends in 15/5 and another starts in 15/5, they do not overlap.
    This is the default django-postgresql behaviour:
    https://docs.djangoproject.com/en/dev/ref/contrib/postgres/fields/#daterangefield
    """
    periods.sort()
    no_overlap = [True]
    for each in range(0, len(periods) - 1):
        latest_start = max(periods[each].lower, periods[each + 1].lower)
        earliest_end = min(periods[each].upper, periods[each + 1].upper)
        delta = earliest_end - latest_start
        if datetime_range:
            no_overlap.append(max(0, delta.total_seconds()) == 0)
        else:
            no_overlap.append(max(0, delta.days) == 0)
    return False if all(no_overlap) else True
