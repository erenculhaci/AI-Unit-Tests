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

if __name__ == '__main__':
    unittest.main()