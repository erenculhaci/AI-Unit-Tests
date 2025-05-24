# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import eat

class TestEatFunction(unittest.TestCase):
    
    def test_example_cases(self):
        """Test the example cases given in the problem description."""
        self.assertEqual(eat(5, 6, 10), [11, 4])
        self.assertEqual(eat(4, 8, 9), [12, 1])
        self.assertEqual(eat(1, 10, 10), [11, 0])
        self.assertEqual(eat(2, 11, 5), [7, 0])
    
    def test_edge_cases(self):
        """Test some edge cases."""
        # When remaining is 0
        self.assertEqual(eat(10, 5, 0), [10, 0])
        
        # When need is 0
        self.assertEqual(eat(7, 0, 3), [7, 3])
        
        # When number is 0
        self.assertEqual(eat(0, 6, 10), [6, 4])
        
        # When all values are 0
        self.assertEqual(eat(0, 0, 0), [0, 0])
        
        # Testing upper bounds of constraints
        self.assertEqual(eat(1000, 1000, 1000), [2000, 0])

if __name__ == "__main__":
    unittest.main()