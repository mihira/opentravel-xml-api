#!/usr/bin/env python

from ota_xml_api.util.date import Period
import unittest
import datetime

class PeriodTC(unittest.TestCase):

    def assert_period(self, period, start, end):
        self.assertEqual(period.start, start.isoformat())
        self.assertEqual(period.end, end.isoformat())

    def test_init_period(self):
        period = Period() #today, tomorrow
        today = datetime.date.today()
        end = datetime.date.fromordinal(today.toordinal() + 1)
        self.assert_period(period, today, end)
        period = Period(15) #today, today + 15
        end = datetime.date.fromordinal(today.toordinal() + 15)
        self.assert_period(period, today, end)
        period = Period(2, -15) #today - 15, today - 13
        start = datetime.date.fromordinal(today.toordinal() - 15)
        end = datetime.date.fromordinal(start.toordinal() + 2)
        self.assert_period(period, start, end)
        period = Period(2, 15) #today + 15, today + 17
        start = datetime.date.fromordinal(today.toordinal() + 15)
        end = datetime.date.fromordinal(start.toordinal() + 2)
        self.assert_period(period, start, end)

if __name__ == '__main__':
    unittest.main()
