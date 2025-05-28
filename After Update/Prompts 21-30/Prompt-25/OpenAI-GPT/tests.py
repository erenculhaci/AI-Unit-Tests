# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    # --- Original Functional Tests ---
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
        self.assertFalse(is_palindrome("Madam"))  # 'M' ≠ 'm'

    # --- Additional Functional Tests ---
    def test_palindrome_with_spaces(self):
        self.assertFalse(is_palindrome("a man a plan a canal panama"))  # literal spaces

    def test_palindrome_with_mixed_case(self):
        self.assertFalse(is_palindrome("RaceCar"))  # case-sensitive

    def test_true_if_case_ignored(self):
        self.assertTrue(is_palindrome("madam".lower()))  # simulate case normalization

    def test_numbers_in_string(self):
        self.assertTrue(is_palindrome("12321"))

    def test_symbols_and_text(self):
        self.assertTrue(is_palindrome("!@#@@#@!"))

    def test_mixed_alnum(self):
        self.assertFalse(is_palindrome("abc123cba"))

    def test_whitespace_only(self):
        self.assertTrue(is_palindrome("     "))

    def test_string_with_newlines(self):
        self.assertFalse(is_palindrome("a\nb\nc"))

    def test_tabbed_string(self):
        self.assertFalse(is_palindrome("a\tb\ta"))

    # --- Invalid Input Tests (Optional Robustness) ---
    def test_none_input(self):
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            is_palindrome(12321)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            is_palindrome(["a", "b", "a"])

if __name__ == "__main__":
    unittest.main()
