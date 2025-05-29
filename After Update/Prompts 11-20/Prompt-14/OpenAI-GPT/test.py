# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(make_palindrome(""), "")

    def test_single_character(self):
        self.assertEqual(make_palindrome("a"), "a")

    def test_already_palindrome(self):
        self.assertEqual(make_palindrome("racecar"), "racecar")

    def test_examples_from_docstring(self):
        self.assertEqual(make_palindrome("cat"), "catac")
        self.assertEqual(make_palindrome("cata"), "catac")

    def test_partial_palindrome_suffix(self):
        self.assertEqual(make_palindrome("banana"), "bananab")  # Düzenlendi

    def test_with_repeating_characters(self):
        self.assertEqual(make_palindrome("aaa"), "aaa")
        self.assertEqual(make_palindrome("aaab"), "aaabaaa")
        self.assertEqual(make_palindrome("aabaa"), "aabaa")

    def test_with_special_characters(self):
        self.assertEqual(make_palindrome("a!b"), "a!b!a")
        self.assertEqual(make_palindrome("12345"), "123454321")  # Düzenlendi
        self.assertEqual(make_palindrome("a@b#c"), "a@b#c#b@a")


    def test_with_spaces(self):
        self.assertEqual(make_palindrome("hello world"), "hello worldlrow olleh")
        self.assertEqual(make_palindrome("a b"), "a b a")

    def test_complex_examples(self):
        self.assertEqual(make_palindrome("abcd"), "abcdcba")
        self.assertEqual(make_palindrome("code"), "codedoc")
        self.assertEqual(make_palindrome("python"), "pythonohtyp")

    def test_with_only_last_char_palindromic(self):
        self.assertEqual(make_palindrome("abcde"), "abcdedcba")
        self.assertEqual(make_palindrome("xyz"), "xyzyx")

    def test_long_string(self):
        long_str = "programming" * 10
        result = make_palindrome(long_str)
        self.assertTrue(result.startswith(long_str))
        self.assertTrue(result == result[::-1])

    def test_with_mixed_case(self):
        self.assertEqual(make_palindrome("aBc"), "aBcBa")  # Düzenlendi
        self.assertEqual(make_palindrome("AbCd"), "AbCdCbA")

if __name__ == "__main__":
    unittest.main()
