# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import sort_array

class TestSortArray(unittest.TestCase):
    def test_empty_array(self):
        # Test with an empty array
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        # Test with a single-element array
        self.assertEqual(sort_array([5]), [5])

    def test_odd_sum_sort_ascending(self):
        # Test with an array where the sum of the first and last elements is odd
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_even_sum_sort_descending(self):
        # Test with an array where the sum of the first and last elements is even
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_large_array(self):
        # Test with a larger array to ensure correct sorting
        self.assertEqual(sort_array([10, 20, 30, 40, 50, 60]), [60, 50, 40, 30, 20, 10])

if __name__ == "__main__":
    unittest.main()