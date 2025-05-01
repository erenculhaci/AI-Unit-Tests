import unittest
from code import valid_date

class TestValidDate(unittest.TestCase):
    
    def test_example_1(self):
        self.assertTrue(valid_date('03-11-2000'))
    
    def test_example_2(self):
        self.assertFalse(valid_date('15-01-2012'))
    
    def test_example_3(self):
        self.assertFalse(valid_date('04-0-2040'))
    
    def test_example_4(self):
        self.assertTrue(valid_date('06-04-2020'))
    
    def test_example_5(self):
        self.assertFalse(valid_date('06/04/2020'))
    
    def test_empty_string(self):
        self.assertFalse(valid_date(''))
    
    def test_invalid_format(self):
        self.assertFalse(valid_date('2020-04-06'))
        self.assertFalse(valid_date('06-04/2020'))
        self.assertFalse(valid_date('06-04-20-20'))
    
    def test_month_limits(self):
        self.assertTrue(valid_date('01-15-2020'))
        self.assertTrue(valid_date('12-15-2020'))
        self.assertFalse(valid_date('00-15-2020'))
        self.assertFalse(valid_date('13-15-2020'))
    
    def test_day_limits_31_days(self):
        # Months with 31 days: 1, 3, 5, 7, 8, 10, 12
        self.assertTrue(valid_date('01-01-2020'))
        self.assertTrue(valid_date('01-31-2020'))
        self.assertFalse(valid_date('01-32-2020'))
        self.assertFalse(valid_date('01-00-2020'))
    
    def test_day_limits_30_days(self):
        # Months with 30 days: 4, 6, 9, 11
        self.assertTrue(valid_date('04-01-2020'))
        self.assertTrue(valid_date('04-30-2020'))
        self.assertFalse(valid_date('04-31-2020'))
        self.assertFalse(valid_date('04-00-2020'))
    
    def test_february(self):
        self.assertTrue(valid_date('02-01-2020'))
        self.assertTrue(valid_date('02-29-2020'))
        self.assertFalse(valid_date('02-30-2020'))
        self.assertFalse(valid_date('02-00-2020'))

if __name__ == '__main__':
    unittest.main()