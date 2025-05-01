# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import unique_digits

class TestUniqueDigits(unittest.TestCase):
    
    def test_example_case_1(self):
        """Test with the first example from the docstring."""
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
    
    def test_example_case_2(self):
        """Test with the second example from the docstring."""
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
    
    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(unique_digits([]), [])
    
    def test_all_odd_digits(self):
        """Test with a list where all numbers have only odd digits."""
        self.assertEqual(unique_digits([1, 3, 5, 7, 9, 13, 15, 17, 19, 35, 79, 111]), 
                         [1, 3, 5, 7, 9, 13, 15, 17, 19, 35, 79, 111])
    
    def test_mixed_numbers(self):
        """Test with a mix of numbers with all odd digits and some even digits."""
        self.assertEqual(unique_digits([11, 22, 33, 44, 55, 66, 77, 88, 99]), 
                         [11, 33, 55, 77, 99])

if __name__ == "__main__":
    unittest.main()