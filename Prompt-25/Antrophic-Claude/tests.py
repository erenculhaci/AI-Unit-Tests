import unittest
from code import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))
    
    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))
    
    def test_two_same_characters(self):
        self.assertTrue(is_palindrome('aa'))
    
    def test_two_different_characters(self):
        self.assertFalse(is_palindrome('ab'))
    
    def test_palindrome_odd_length(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('abcba'))
    
    def test_palindrome_even_length(self):
        self.assertTrue(is_palindrome('abba'))
        self.assertTrue(is_palindrome('abccba'))
    
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))
        self.assertFalse(is_palindrome('hello'))
    
    def test_repeated_characters(self):
        self.assertTrue(is_palindrome('aaaaa'))

if __name__ == '__main__':
    unittest.main()