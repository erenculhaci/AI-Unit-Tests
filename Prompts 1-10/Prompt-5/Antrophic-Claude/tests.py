import unittest
from code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):
    def test_small_input(self):
        # Test with small input n = 3
        self.assertEqual(even_odd_palindrome(3), (1, 2))
    
    def test_medium_input(self):
        # Test with medium input n = 12
        self.assertEqual(even_odd_palindrome(12), (4, 6))
    
    def test_large_input(self):
        # Test with larger input n = 100
        # Let's list all palindromes up to 100:
        # Single digits: 1, 2, 3, 4, 5, 6, 7, 8, 9
        # Double digits: 11, 22, 33, 44, 55, 66, 77, 88, 99
        # Even palindromes: 2, 4, 6, 8, 22, 44, 66, 88 (8 total)
        # Odd palindromes: 1, 3, 5, 7, 9, 11, 33, 55, 77, 99 (10 total)
        self.assertEqual(even_odd_palindrome(100), (8, 10))
    
    def test_single_input(self):
        # Test with input n = 1
        self.assertEqual(even_odd_palindrome(1), (0, 1))
    
    def test_edge_case(self):
        # Test with input n = 22
        # Palindromes: 1-9, 11, 22
        # Even palindromes: 2, 4, 6, 8, 22 (5 total)
        # Odd palindromes: 1, 3, 5, 7, 9, 11 (6 total)
        self.assertEqual(even_odd_palindrome(22), (5, 6))

if __name__ == "__main__":
    unittest.main()