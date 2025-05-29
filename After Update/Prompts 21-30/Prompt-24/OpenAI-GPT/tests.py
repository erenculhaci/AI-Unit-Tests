# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import valid_date


class TestValidDate(unittest.TestCase):

    # --- Valid Functional Tests ---
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
        self.assertTrue(valid_date('01-01-2020'))
        self.assertTrue(valid_date('01-31-2020'))
        self.assertFalse(valid_date('01-32-2020'))
        self.assertFalse(valid_date('01-00-2020'))

    def test_day_limits_30_days(self):
        self.assertTrue(valid_date('04-01-2020'))
        self.assertTrue(valid_date('04-30-2020'))
        self.assertFalse(valid_date('04-31-2020'))
        self.assertFalse(valid_date('04-00-2020'))

    def test_february(self):
        self.assertTrue(valid_date('02-01-2020'))
        self.assertTrue(valid_date('02-29-2020'))
        self.assertFalse(valid_date('02-30-2020'))
        self.assertFalse(valid_date('02-00-2020'))

    def test_all_months_31_days(self):
        for month in ['01', '03', '05', '07', '08', '10', '12']:
            self.assertTrue(valid_date(f'{month}-31-2020'))
            self.assertFalse(valid_date(f'{month}-32-2020'))

    def test_all_months_30_days(self):
        for month in ['04', '06', '09', '11']:
            self.assertTrue(valid_date(f'{month}-30-2020'))
            self.assertFalse(valid_date(f'{month}-31-2020'))

    def test_leading_zeros(self):
        self.assertTrue(valid_date('01-01-2020'))
        self.assertTrue(valid_date('09-09-2020'))
        self.assertFalse(valid_date('1-1-2020'))
        self.assertFalse(valid_date('9-9-2020'))

    def test_negative_values(self):
        self.assertFalse(valid_date('-1-15-2020'))
        self.assertFalse(valid_date('01--5-2020'))
        self.assertFalse(valid_date('01-15--2020'))

    def test_non_numeric_values(self):
        self.assertFalse(valid_date('ab-15-2020'))
        self.assertFalse(valid_date('01-cd-2020'))
        self.assertFalse(valid_date('01-15-abcd'))

    def test_special_characters(self):
        self.assertFalse(valid_date('01!15-2020'))
        self.assertFalse(valid_date('01-15@2020'))
        self.assertFalse(valid_date('01-15-20#0'))

    def test_different_separators(self):
        self.assertFalse(valid_date('01/15/2020'))
        self.assertFalse(valid_date('01.15.2020'))
        self.assertFalse(valid_date('01 15 2020'))

    def test_missing_parts(self):
        self.assertFalse(valid_date('01-15'))
        self.assertFalse(valid_date('01-15-'))
        self.assertFalse(valid_date('-15-2020'))
        self.assertFalse(valid_date('01--2020'))

    def test_extra_parts(self):
        self.assertFalse(valid_date('01-15-2020-extra'))
        self.assertFalse(valid_date('extra-01-15-2020'))

    def test_year_variations(self):
        self.assertTrue(valid_date('01-15-0001'))
        self.assertTrue(valid_date('01-15-9999'))
        self.assertFalse(valid_date('01-15-20'))

    # --- Invalid Input Tests ---
    def test_non_string_input_integer(self):
        with self.assertRaises(AttributeError):
            valid_date(123)

    def test_non_string_input_list(self):
        with self.assertRaises(AttributeError):
            valid_date(['01', '15', '2020'])

    def test_non_string_input_none(self):
        with self.assertRaises(AttributeError):
            valid_date(None)

    def test_non_string_input_dict(self):
        with self.assertRaises(AttributeError):
            valid_date({'month': '01', 'day': '15', 'year': '2020'})

    def test_non_string_input_boolean(self):
        with self.assertRaises(AttributeError):
            valid_date(True)

    def test_non_string_input_float(self):
        with self.assertRaises(AttributeError):
            valid_date(3.14)

    # --- Edge Cases ---
    def test_whitespace_handling(self):
        self.assertFalse(valid_date(' 01-15-2020'))
        self.assertFalse(valid_date('01-15-2020 '))
        self.assertFalse(valid_date('01 -15-2020'))

    def test_extreme_dates(self):
        self.assertTrue(valid_date('12-31-9999'))
        self.assertTrue(valid_date('01-01-0001'))
        self.assertFalse(valid_date('13-01-2020'))
        self.assertFalse(valid_date('12-32-2020'))


if __name__ == '__main__':
    unittest.main()