# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import will_it_fly

class TestWillItFly(unittest.TestCase):
    
    def test_unbalanced_within_weight(self):
        """Test with an unbalanced list that is within weight limit."""
        self.assertFalse(will_it_fly([1, 2], 5))
    
    def test_balanced_exceeds_weight(self):
        """Test with a balanced list that exceeds the weight limit."""
        self.assertFalse(will_it_fly([3, 2, 3], 1))
    
    def test_balanced_within_weight(self):
        """Test with a balanced list that is within weight limit."""
        self.assertTrue(will_it_fly([3, 2, 3], 9))
    
    def test_single_element_list(self):
        """Test with a single element list (which is always balanced)."""
        self.assertTrue(will_it_fly([3], 5))
        
    def test_empty_list(self):
        """Test with an empty list (which is balanced by definition)."""
        self.assertTrue(will_it_fly([], 5))
        
    def test_exact_weight_limit(self):
        """Test with a balanced list that exactly matches the weight limit."""
        self.assertTrue(will_it_fly([2, 1, 2], 5))
        
    def test_even_length_balanced_list(self):
        """Test with a balanced list of even length."""
        self.assertTrue(will_it_fly([1, 2, 2, 1], 10))
        
    def test_unbalanced_complex_list(self):
        """Test with a more complex unbalanced list."""
        self.assertFalse(will_it_fly([1, 2, 3, 4, 5], 20))
        
    def test_negative_numbers_balanced(self):
        """Test with balanced list containing negative numbers."""
        self.assertTrue(will_it_fly([-1, 0, -1], 5))
        
    def test_negative_numbers_exceed_weight(self):
        """Test with balanced list of negative numbers that still exceeds weight."""
        self.assertFalse(will_it_fly([-5, -10, -5], 15))
        
    def test_zero_weight_limit(self):
        """Test with zero weight limit - only empty list should fly."""
        self.assertTrue(will_it_fly([], 0))
        self.assertFalse(will_it_fly([0, 0], 0))
        
    def test_large_balanced_list(self):
        """Test with a large balanced list."""
        big_list = [i for i in range(100)] + [i for i in range(99, -1, -1)]
        self.assertFalse(will_it_fly(big_list, 9000))  # Sum would be 9900

if __name__ == "__main__":
    unittest.main()