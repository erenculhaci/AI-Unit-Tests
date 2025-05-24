# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import get_row

class TestGetRow(unittest.TestCase):
    def test_multiple_occurrences(self):
        # Test with multiple occurrences of the target value
        data = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ]
        self.assertEqual(get_row(data, 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(get_row([], 1), [])

    def test_nested_empty_lists(self):
        # Test with nested empty lists
        data = [[], [1], [1, 2, 3]]
        self.assertEqual(get_row(data, 3), [(2, 2)])

    def test_no_occurrences(self):
        # Test when the target value does not exist in the data
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(get_row(data, 10), [])

if __name__ == "__main__":
    unittest.main()