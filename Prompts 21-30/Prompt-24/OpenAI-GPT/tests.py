# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_dates(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertTrue(valid_date('06-04-2020'))

    def test_invalid_months(self):
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('00-01-2012'))

    def test_invalid_day(self):
        self.assertFalse(valid_date('04-0-2040'))
        self.assertFalse(valid_date('02-30-2020'))  # February max 29

    def test_invalid_format(self):
        self.assertFalse(valid_date('06/04/2020'))
        self.assertFalse(valid_date('06042020'))

    def test_edge_cases(self):
        self.assertTrue(valid_date('02-29-2020'))  # Accepts up to 29 for February
        self.assertFalse(valid_date('02-00-2020'))  # Invalid day

if __name__ == "__main__":
    unittest.main()
