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
        self.assertEqual(original, [2, 4, 3, 0, 1, 5])
    
    def test_even_sum_descending_sort(self):
        """Test with array where first+last is even (should sort descending)."""
        original = [2, 4, 3, 0, 1, 5, 6]
        expected = [6, 5, 4, 3, 2, 1, 0]
        result = sort_array(original)
        self.assertEqual(result, expected)
        self.assertEqual(original, [2, 4, 3, 0, 1, 5, 6])
    
    def test_additional_cases(self):
        """Test additional cases for more coverage."""
        self.assertEqual(sort_array([1, 3, 5, 7, 9]), [9, 7, 5, 3, 1])  # even sum (1+9=10)
        self.assertEqual(sort_array([2, 3, 5, 7, 9]), [2, 3, 5, 7, 9])  # odd sum (2+9=11)
        self.assertEqual(sort_array([7, 2, 2, 5, 4, 7, 6]), [2, 2, 4, 5, 6, 7, 7])  # odd sum (7+6=13)
    
    def test_negative_numbers(self):
        """Test with arrays containing negative numbers."""
        with self.assertRaises(ValueError):
            sort_array([-1, 2, 3, 4])
    
    def test_large_array(self):
        """Test with a very large array."""
        large_array = list(range(1000))  # sum = 0+999 = 999 → odd → ascending
        result = sort_array(large_array)
        self.assertEqual(result, list(range(1000)))
    
    def test_zeros_at_endpoints(self):
        """Test with arrays containing zeros at various positions."""
        self.assertEqual(sort_array([0, 2, 3, 4, 5]), [0, 2, 3, 4, 5])     # odd sum (0+5=5)
        self.assertEqual(sort_array([2, 3, 4, 0]), [4, 3, 2, 0])           # even sum (2+0=2)
        self.assertEqual(sort_array([0, 3, 5, 2, 0]), [5, 3, 2, 0, 0])     # even sum (0+0=0)
    
    def test_same_endpoints(self):
        """Test with arrays where first and last elements are equal."""
        self.assertEqual(sort_array([3, 1, 4, 5, 3]), [5, 4, 3, 3, 1])     # even sum (3+3=6)
        self.assertEqual(sort_array([2, 5, 1, 3, 2]), [5, 3, 2, 2, 1])     # even sum (2+2=4)
    
    def test_mixed_types(self):
        """Test with arrays containing mixed types."""
        with self.assertRaises(TypeError):
            sort_array([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            sort_array([1, 2.5, 3, 4])

if __name__ == '__main__':
    unittest.main()
