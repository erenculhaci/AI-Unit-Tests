# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import is_sorted

class TestIsSorted(unittest.TestCase):
    
    def test_single_element_list(self):
        """Test with a single element list."""
        self.assertTrue(is_sorted([5]))
    
    def test_sorted_lists(self):
        """Test with sorted lists."""
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
    
    def test_unsorted_lists(self):
        """Test with unsorted lists."""
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
        self.assertFalse(is_sorted([5, 4, 3, 2, 1]))
    
    def test_allowed_duplicates(self):
        """Test with lists containing allowed number of duplicates (at most 2 of each number)."""
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
        self.assertTrue(is_sorted([1, 1, 2, 2, 3, 3, 4]))
    
    def test_too_many_duplicates(self):
        """Test with lists containing too many duplicates (more than 2 of a number)."""
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))
        self.assertFalse(is_sorted([1, 1, 1, 2, 3, 4]))
        self.assertFalse(is_sorted([1, 2, 3, 3, 3, 4]))

if __name__ == "__main__":
    unittest.main()