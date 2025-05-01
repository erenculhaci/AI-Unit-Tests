# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import unique_digits

class TestUniqueDigits(unittest.TestCase):
    def test_mixed_numbers(self):
        # Test with a mix of numbers with and without even digits
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_all_numbers_with_even_digits(self):
        # Test with numbers that all contain even digits
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_all_numbers_without_even_digits(self):
        # Test with numbers that all do not contain even digits
        self.assertEqual(unique_digits([11, 33, 55, 77]), [11, 33, 55, 77])

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(unique_digits([]), [])

    def test_single_number(self):
        # Test with a single number
        self.assertEqual(unique_digits([135]), [135])

if __name__ == "__main__":
    unittest.main()