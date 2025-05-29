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
    
    def test_single_digit_numbers(self):
        """Test with only single-digit numbers."""
        self.assertEqual(unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]), 
                         [1, 3, 5, 7, 9])
    
    def test_large_numbers(self):
        """Test with large numbers with all odd digits."""
        self.assertEqual(unique_digits([11111, 33333, 55555, 77777, 99999]), 
                         [11111, 33333, 55555, 77777, 99999])
    
    def test_zeros_in_numbers(self):
        """Test with numbers containing zeros (which are even digits)."""
        self.assertEqual(unique_digits([101, 303, 505, 707, 909]), 
                         [])
    
    def test_sorting_order(self):
        """Test that the output is sorted in increasing order."""
        self.assertEqual(unique_digits([99, 55, 33, 77, 11, 1, 3, 5]), 
                         [1, 3, 5, 11, 33, 55, 77, 99])
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers."""
        self.assertEqual(unique_digits([33, 33, 55, 55, 77, 77]), 
                         [33, 33, 55, 55, 77, 77])
    
    def test_edge_cases(self):
        """Test with edge cases like very large numbers."""
        self.assertEqual(unique_digits([9999999999, 1, 3333333333]), 
                         [1, 3333333333, 9999999999])
    
    def test_numbers_ending_with_odd(self):
        """Test numbers ending with odd digits but containing even digits."""
        self.assertEqual(unique_digits([123, 345, 567, 789]), 
                         [])

if __name__ == "__main__":
    unittest.main()