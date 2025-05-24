# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import sort_array

class TestSortArray(unittest.TestCase):
    
    def test_empty_array(self):
        """Test with an empty array."""
        self.assertEqual(sort_array([]), [])
    
    def test_single_element_array(self):
        """Test with an array containing a single element."""
        self.assertEqual(sort_array([5]), [5])
    
    def test_odd_sum_ascending_sort(self):
        """Test with array where first+last is odd (should sort ascending)."""
        original = [2, 4, 3, 0, 1, 5]
        expected = [0, 1, 2, 3, 4, 5]
        result = sort_array(original)
        self.assertEqual(result, expected)
        # Verify original array wasn't modified
        self.assertEqual(original, [2, 4, 3, 0, 1, 5])
    
    def test_even_sum_descending_sort(self):
        """Test with array where first+last is even (should sort descending)."""
        original = [2, 4, 3, 0, 1, 5, 6]
        expected = [6, 5, 4, 3, 2, 1, 0]
        result = sort_array(original)
        self.assertEqual(result, expected)
        # Verify original array wasn't modified
        self.assertEqual(original, [2, 4, 3, 0, 1, 5, 6])
    
    def test_additional_cases(self):
        """Test additional cases for more coverage."""
        # Case 1: Even sum
        self.assertEqual(sort_array([1, 3, 5, 7, 9]), [9, 7, 5, 3, 1])
        
        # Case 2: Odd sum
        self.assertEqual(sort_array([2, 3, 5, 7, 9]), [2, 3, 5, 7, 9])
        
        # Case 3: Duplicate values with odd sum
        self.assertEqual(sort_array([7, 2, 2, 5, 4, 7, 6]), [2, 2, 4, 5, 6, 7, 7])

if __name__ == '__main__':
    unittest.main()