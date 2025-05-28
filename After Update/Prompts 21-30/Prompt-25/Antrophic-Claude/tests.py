# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    
    # --- Valid Functional Tests ---
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))
    
    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('z'))
    
    def test_two_same_characters(self):
        self.assertTrue(is_palindrome('aa'))
        self.assertTrue(is_palindrome('zz'))
    
    def test_two_different_characters(self):
        self.assertFalse(is_palindrome('ab'))
        self.assertFalse(is_palindrome('za'))
    
    def test_palindrome_odd_length(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('abcba'))
        self.assertTrue(is_palindrome('racecar'))
    
    def test_palindrome_even_length(self):
        self.assertTrue(is_palindrome('abba'))
        self.assertTrue(is_palindrome('abccba'))
        self.assertTrue(is_palindrome('noon'))
    
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('world'))
    
    def test_repeated_characters(self):
        self.assertTrue(is_palindrome('aaaaa'))
        self.assertTrue(is_palindrome('bbbbb'))
    
    def test_case_sensitivity(self):
        self.assertFalse(is_palindrome('Aa'))
        self.assertFalse(is_palindrome('AbA'))
        self.assertTrue(is_palindrome('AaA'))
    
    def test_mixed_case_palindromes(self):
        self.assertTrue(is_palindrome('ABA'))
        self.assertTrue(is_palindrome('ABBA'))
        self.assertFalse(is_palindrome('ABa'))
    
    def test_numeric_palindromes(self):
        self.assertTrue(is_palindrome('12321'))
        self.assertTrue(is_palindrome('1221'))
        self.assertFalse(is_palindrome('12345'))
    
    def test_special_characters(self):
        self.assertTrue(is_palindrome('!@#@!'))
        self.assertTrue(is_palindrome('a!a'))
        self.assertFalse(is_palindrome('a!b'))
    
    def test_long_palindromes(self):
        self.assertTrue(is_palindrome('abcdedcba'))
        self.assertTrue(is_palindrome('abcdefedcba'))
        self.assertFalse(is_palindrome('abcdefghijk'))
    
    def test_palindromes_with_spaces(self):
        self.assertTrue(is_palindrome('a a'))
        self.assertTrue(is_palindrome(' a '))
        self.assertFalse(is_palindrome('a b'))
    
    def test_mixed_alphanumeric(self):
        self.assertTrue(is_palindrome('a1a'))
        self.assertTrue(is_palindrome('1a1'))
        self.assertFalse(is_palindrome('a1b'))
    
    # --- Invalid Input Tests ---
    def test_non_string_input_integer(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)
    
    def test_non_string_input_list(self):
        with self.assertRaises(TypeError):
            is_palindrome(['a', 'b', 'a'])
    
    def test_non_string_input_none(self):
        with self.assertRaises(TypeError):
            is_palindrome(None)
    
    def test_non_string_input_dict(self):
        with self.assertRaises(TypeError):
            is_palindrome({'key': 'value'})
    
    def test_non_string_input_boolean(self):
        with self.assertRaises(TypeError):
            is_palindrome(True)
    
    def test_non_string_input_float(self):
        with self.assertRaises(TypeError):
            is_palindrome(3.14)
    
    # --- Edge Cases ---
    def test_whitespace_only(self):
        self.assertTrue(is_palindrome(' '))
        self.assertTrue(is_palindrome('   '))
    
    def test_newline_characters(self):
        self.assertTrue(is_palindrome('\n'))
        self.assertTrue(is_palindrome('a\na'))
    
    def test_tab_characters(self):
        self.assertTrue(is_palindrome('\t'))
        self.assertTrue(is_palindrome('a\ta'))
    
    def test_unicode_characters(self):
        self.assertTrue(is_palindrome('αβα'))
        self.assertTrue(is_palindrome('café'))
    
    def test_boundary_cases(self):
        self.assertTrue(is_palindrome('a' * 1000))
        self.assertTrue(is_palindrome('ab' * 500 + 'ba' * 500))

if __name__ == '__main__':
    unittest.main()