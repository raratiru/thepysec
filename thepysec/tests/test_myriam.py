#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/myriam/tests/test_datetime.py
#
#       Creation Date : Sat 26 Oct 2019 08:56:39 PM EEST (20:56)
#
#       Last Modified : Sat 26 Oct 2019 09:22:52 PM EEST (21:22)
#
# ==============================================================================

from thepysec import myriam
from psycopg2.extras import DateTimeTZRange, DateRange
from datetime import date, datetime


def test_datetime_false():
    datetime_periods = [
        DateTimeTZRange(datetime(2400, 2, 10, 15, 00), datetime(2400, 2, 10, 17, 00)),
        DateTimeTZRange(datetime(2400, 2, 20, 15, 00), datetime(2400, 2, 29, 15, 00)),
        DateTimeTZRange(datetime(2400, 2, 12, 15, 00), datetime(2400, 2, 20, 15, 00)),
        DateTimeTZRange(datetime(2400, 2, 10, 17, 00), datetime(2400, 2, 12, 15, 00)),
    ]
    assert myriam.validate_overlap(datetime_periods, datetime_range=True) is False


def test_datetime_true():
    datetime_periods = [
        DateTimeTZRange(datetime(2400, 2, 10, 15, 00), datetime(2400, 2, 10, 17, 00)),
        DateTimeTZRange(datetime(2400, 2, 20, 15, 00), datetime(2400, 2, 29, 15, 00)),
        DateTimeTZRange(datetime(2400, 2, 12, 15, 00), datetime(2400, 2, 20, 15, 00)),
        DateTimeTZRange(datetime(2400, 2, 10, 16, 59), datetime(2400, 2, 12, 15, 00)),
    ]
    assert myriam.validate_overlap(datetime_periods, datetime_range=True) is True


def test_date_false():
    date_periods = [
        DateRange(date(2400, 2, 10), date(2400, 2, 11)),
        DateRange(date(2400, 2, 21), date(2400, 2, 29)),
        DateRange(date(2400, 2, 12), date(2400, 2, 20)),
        DateRange(date(2400, 2, 11), date(2400, 2, 12)),
    ]
    assert myriam.validate_overlap(date_periods, datetime_range=False) is False


def test_date_true():
    date_periods = [
        DateRange(date(2400, 2, 10), date(2400, 2, 11)),
        DateRange(date(2400, 2, 19), date(2400, 2, 29)),
        DateRange(date(2400, 2, 12), date(2400, 2, 20)),
        DateRange(date(2400, 2, 11), date(2400, 2, 12)),
    ]
    assert myriam.validate_overlap(date_periods, datetime_range=False) is True
