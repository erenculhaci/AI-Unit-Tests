# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        # Test with an empty string
        self.assertEqual(make_palindrome(''), '')

    def test_already_palindrome(self):
        # Test with a string that is already a palindrome
        self.assertEqual(make_palindrome('racecar'), 'racecar')

    def test_non_palindromic_string(self):
        # Test with a non-palindromic string
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_partial_palindromic_suffix(self):
        # Test with a string that has a partial palindromic suffix
        self.assertEqual(make_palindrome('cata'), 'catac')

    def test_single_character(self):
        # Test with a single character string
        self.assertEqual(make_palindrome('a'), 'a')

if __name__ == "__main__":
    unittest.main()