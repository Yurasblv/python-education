"""Module for testing date"""
import datetime
import freezegun
from tests.to_test import time_of_day


@freezegun.freeze_time("2018-07-13 16:52:35")
def test_afternoon():
    """Tests the day cycle"""
    assert time_of_day() == 'afternoon'
    assert time_of_day() != 'night'


@freezegun.freeze_time("2018-07-13 00:52:35")
def test_night():
    """Tests the day cycle"""
    assert time_of_day() != 'morning'
    assert time_of_day() == 'night'


@freezegun.freeze_time(datetime.datetime(year=2013, month=8, day=14, hour=11, minute=42, second=00))
def test_morning():
    """Tests the day cycle"""
    assert time_of_day() != 'afternoon'
    assert time_of_day() != 'night'
