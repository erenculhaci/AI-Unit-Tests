# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import reverse_delete


class TestReverseDelete(unittest.TestCase):

    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test_example_2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_example_3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

    def test_empty_string(self):
        self.assertEqual(reverse_delete("", "abc"), ('', True))

    def test_empty_chars_to_delete(self):
        self.assertEqual(reverse_delete("abcba", ""), ('abcba', True))

    def test_delete_all_chars(self):
        self.assertEqual(reverse_delete("abc", "abc"), ('', True))

    def test_case_sensitivity(self):
        self.assertEqual(reverse_delete("AbCdE", "ae"), ('AbCdE', False))  # corrected expected result

    def test_palindrome_after_deletion(self):
        self.assertEqual(reverse_delete("kitten", "ten"), ('ki', False))
        self.assertEqual(reverse_delete("racecar", "ae"), ('rccr', True))

    def test_single_character_string(self):
        self.assertEqual(reverse_delete("a", "a"), ('', True))
        self.assertEqual(reverse_delete("a", "b"), ('a', True))

    def test_single_character_deletion(self):
        self.assertEqual(reverse_delete("abcba", "c"), ('abba', True))
        self.assertEqual(reverse_delete("hello", "l"), ('heo', False))

    def test_no_characters_to_delete(self):
        self.assertEqual(reverse_delete("hello", "xyz"), ('hello', False))
        self.assertEqual(reverse_delete("racecar", "xyz"), ('racecar', True))

    def test_repeated_characters(self):
        self.assertEqual(reverse_delete("aabbcc", "ac"), ('bb', True))
        self.assertEqual(reverse_delete("aaabbbccc", "b"), ('aaaccc', False))  # corrected expectation

    def test_duplicate_chars_in_deletion_set(self):
        self.assertEqual(reverse_delete("abcde", "aaa"), ('bcde', False))
        self.assertEqual(reverse_delete("hello", "lll"), ('heo', False))

    def test_palindrome_variations(self):
        self.assertEqual(reverse_delete("madam", "m"), ('ada', True))
        self.assertEqual(reverse_delete("level", "l"), ('eve', True))
        self.assertEqual(reverse_delete("noon", "n"), ('oo', True))

    def test_mixed_case_palindromes(self):
        self.assertEqual(reverse_delete("Aa", ""), ('Aa', False))  # corrected: "Aa" is not a palindrome case-sensitively
        self.assertEqual(reverse_delete("AaA", ""), ('AaA', True))

    def test_long_strings(self):
        self.assertEqual(reverse_delete("abcdefghijklmnop", "aceg"), ('bdfhijklmnop', False))
        self.assertEqual(reverse_delete("abccba", ""), ('abccba', True))

    def test_all_same_character(self):
        self.assertEqual(reverse_delete("aaaa", "a"), ('', True))
        self.assertEqual(reverse_delete("aaaa", "b"), ('aaaa', True))

    def test_special_characters(self):
        self.assertEqual(reverse_delete("a!b!a", "!"), ('aba', True))
        self.assertEqual(reverse_delete("a@b#c", "@#"), ('abc', False))

    # --- Invalid Input Tests ---
    def test_non_string_input_s_integer(self):
        with self.assertRaises(TypeError):
            reverse_delete(123, "a")

    def test_non_string_input_c_integer(self):
        with self.assertRaises(TypeError):
            reverse_delete("hello", 123)

    def test_non_string_input_s_list(self):
        with self.assertRaises(TypeError):
            reverse_delete(["hello"], "a")

    def test_non_string_input_c_list(self):
        with self.assertRaises(TypeError):
            reverse_delete("hello", ["a"])

    def test_non_string_input_s_none(self):
        with self.assertRaises(TypeError):
            reverse_delete(None, "a")

    def test_non_string_input_c_none(self):
        with self.assertRaises(TypeError):
            reverse_delete("hello", None)

    def test_non_string_input_both_none(self):
        with self.assertRaises(TypeError):
            reverse_delete(None, None)

    # --- Edge Cases ---
    def test_both_empty_strings(self):
        self.assertEqual(reverse_delete("", ""), ('', True))

    def test_numeric_strings(self):
        self.assertEqual(reverse_delete("12321", "1"), ('232', True))
        self.assertEqual(reverse_delete("123456", "24"), ('1356', False))

    def test_order_preservation(self):
        self.assertEqual(reverse_delete("abcdef", "bdf"), ('ace', False))
        self.assertEqual(reverse_delete("fedcba", "bdf"), ('eca', False))


if __name__ == '__main__':
    unittest.main()
