# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import is_sorted  # Adjust the import path if necessary

class TestIsSorted(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(is_sorted([5]))  # Single element list

    def test_sorted_no_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))  # Sorted list with no duplicates

    def test_unsorted_list(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))  # Unsorted list

    def test_sorted_with_valid_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))  # Sorted list with valid duplicates

    def test_sorted_with_invalid_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))  # Sorted list with invalid duplicates

if __name__ == '__main__':
    unittest.main()