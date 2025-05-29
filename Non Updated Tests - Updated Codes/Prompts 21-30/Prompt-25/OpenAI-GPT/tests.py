# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_char(self):
        self.assertTrue(is_palindrome("x"))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome("abba"))

    def test_odd_length_palindrome(self):
        self.assertTrue(is_palindrome("aba"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("zbcd"))

    def test_repeated_characters(self):
        self.assertTrue(is_palindrome("aaaaa"))

    def test_case_sensitive(self):
        self.assertFalse(is_palindrome("Madam"))

if __name__ == "__main__":
    unittest.main()
