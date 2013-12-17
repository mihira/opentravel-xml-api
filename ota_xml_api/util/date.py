#!/usr/bin/env python

"""
This module contains classes/functions related to date
"""

from datetime import date

class Period(object):
    def __init__(self, days=1, start_gap=0):
        today_ord = date.today().toordinal()
        start_ord = today_ord + start_gap
        end_ord = start_ord + days
        self._start = date.fromordinal(start_ord)
        self._end = date.fromordinal(end_ord)

    def get_start(self):
        return self._start.isoformat()
    start = property(get_start, doc='Start date string variable')

    def get_end(self):
        return self._end.isoformat()
    end = property(get_end, doc='End date string variable')
