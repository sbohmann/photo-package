import unittest
from datetime import datetime

import iso_datetime


class TestIsoDatetime(unittest.TestCase):
    def test_simple_positive_cases(self):
        self.assertEqual(
            datetime(2012, 2, 29, 1, 23, 59, 671230),
            iso_datetime.parse('2012-02-29T01:23:59.67123'))

        self.assertEqual(
            datetime(2012, 2, 29, 1, 23, 59, 671237),
            iso_datetime.parse('2012-02-29T01:23:59.671237'))

        self.assertEqual(
            datetime(2012, 2, 29, 1, 23, 59),
            iso_datetime.parse('2012-02-29T01:23:59'))

        self.assertEqual(
            datetime(2012, 2, 29, 1, 23),
            iso_datetime.parse('2012-02-29T01:23'))

    def test_simple_errors(self):
        for input in ['2012-02-29T01:23:59.',
                      '2012-02-29T01:23:59.6712371',
                      '2012-02-29T01:23:',
                      '2012-02-29T01']:
            try:
                iso_datetime.parse(input)
            except ValueError:
                continue
            raise AssertionError('Expected exception on parsing input ' + input)
