# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    
    def test_empty_string(self):
        """Test that an empty string returns an empty string."""
        self.assertEqual(make_palindrome(""), "")
    
    def test_single_character(self):
        """Test that a single character returns the same character."""
        self.assertEqual(make_palindrome("a"), "a")
    
    def test_already_palindrome(self):
        """Test that a string that is already a palindrome returns the same string."""
        self.assertEqual(make_palindrome("racecar"), "racecar")
    
    def test_examples_from_docstring(self):
        """Test the examples provided in the function docstring."""
        self.assertEqual(make_palindrome("cat"), "catac")
        self.assertEqual(make_palindrome("cata"), "catac")
    
    def test_partial_palindrome_suffix(self):
        """Test with a string that has a palindromic suffix longer than one character."""
        self.assertEqual(make_palindrome("banana"), "bananabanab")
        # Explanation: In "banana", "ana" is a palindromic suffix
        # So we take "ban" (the prefix), reverse it to "nab", and append it

if __name__ == "__main__":
    unittest.main()