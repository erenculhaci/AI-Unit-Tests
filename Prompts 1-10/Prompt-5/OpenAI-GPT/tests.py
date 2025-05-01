import unittest
from code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_example_2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_single_digit(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    def test_no_palindrome(self):
        self.assertEqual(even_odd_palindrome(0), (0, 0))

    def test_medium_number(self):
        self.assertEqual(even_odd_palindrome(50), (6, 7))

if __name__ == '__main__':
    unittest.main()