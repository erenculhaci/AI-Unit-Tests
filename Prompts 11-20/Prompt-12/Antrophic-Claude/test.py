# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import get_row

class TestGetRow(unittest.TestCase):
    
    def test_example_from_docstring(self):
        """Test the first example provided in the function docstring."""
        lst = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ]
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        self.assertEqual(get_row(lst, 1), expected)
    
    def test_empty_input(self):
        """Test with an empty list as input."""
        self.assertEqual(get_row([], 1), [])
    
    def test_with_empty_rows(self):
        """Test with a list containing empty rows."""
        lst = [[], [1], [1, 2, 3]]
        self.assertEqual(get_row(lst, 3), [(2, 2)])
    
    def test_no_occurrences(self):
        """Test when the target value doesn't exist in the list."""
        lst = [
            [2, 3, 4],
            [5, 6, 7],
            [8, 9, 10]
        ]
        self.assertEqual(get_row(lst, 1), [])

if __name__ == "__main__":
    unittest.main()