# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import valid_date

class TestValidDate(unittest.TestCase):

    # --- Valid Cases ---
    def test_valid_dates(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertTrue(valid_date('12-31-2022'))
        self.assertTrue(valid_date('01-01-1900'))

    def test_valid_day_limits_per_month(self):
        self.assertTrue(valid_date('01-31-2020'))
        self.assertTrue(valid_date('04-30-2020'))
        self.assertTrue(valid_date('02-29-2020'))

    # --- Invalid Month Values ---
    def test_invalid_months(self):
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('00-01-2012'))
        self.assertFalse(valid_date('13-01-2022'))

    # --- Invalid Day Values ---
    def test_invalid_day(self):
        self.assertFalse(valid_date('04-0-2040'))
        self.assertFalse(valid_date('02-30-2020'))
        self.assertFalse(valid_date('04-31-2020'))
        self.assertFalse(valid_date('11-32-2020'))
        self.assertFalse(valid_date('01-32-2020'))

    # --- Invalid Format Cases ---
    def test_invalid_format(self):
        self.assertFalse(valid_date('06/04/2020'))
        self.assertFalse(valid_date('06042020'))
        self.assertFalse(valid_date('6-4-2020'))
        self.assertFalse(valid_date('06-04-20'))
        self.assertFalse(valid_date('06-04-202'))
        self.assertFalse(valid_date('06-04-20201'))

    # --- Edge Cases ---
    def test_empty_string(self):
        self.assertFalse(valid_date(""))

    def test_whitespace_input(self):
        self.assertFalse(valid_date("   "))

    def test_missing_parts(self):
        self.assertFalse(valid_date("-04-2020"))
        self.assertFalse(valid_date("06--2020"))
        self.assertFalse(valid_date("06-04-"))

    # --- Non-Numeric Input ---
    def test_non_numeric_values(self):
        self.assertFalse(valid_date("aa-bb-cccc"))
        self.assertFalse(valid_date("mm-12-2020"))
        self.assertFalse(valid_date("12-dd-2020"))

    def test_symbols_in_date(self):
        self.assertFalse(valid_date("01-@1-2020"))
        self.assertFalse(valid_date("$$-12-2020"))

if __name__ == "__main__":
    unittest.main()
