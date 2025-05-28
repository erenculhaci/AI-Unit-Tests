# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(
            sorted_list_sum(["aa", "a", "aaa"]),
            ["aa"]
        )

    def test_example_2(self):
        self.assertEqual(
            sorted_list_sum(["ab", "a", "aaa", "cd"]),
            ["ab", "cd"]
        )

    def test_empty_list(self):
        self.assertEqual(
            sorted_list_sum([]),
            []
        )

    def test_no_even_length_strings(self):
        self.assertEqual(
            sorted_list_sum(["a", "abc", "abcde"]),
            []
        )

    def test_all_even_length_strings(self):
        self.assertEqual(
            sorted_list_sum(["ab", "abcd", "abcdef"]),
            ["ab", "abcd", "abcdef"]
        )

    def test_mixed_length_strings(self):
        self.assertEqual(
            sorted_list_sum(["abcd", "a", "ab", "abc", "abcdef"]),
            ["ab", "abcd", "abcdef"]
        )

    def test_same_length_alphabetical_order(self):
        self.assertEqual(
            sorted_list_sum(["cd", "ab", "ef", "xy"]),
            ["ab", "cd", "ef", "xy"]
        )

    def test_duplicates(self):
        self.assertEqual(
            sorted_list_sum(["ab", "cd", "ab", "ef", "cd"]),
            ["ab", "ab", "cd", "cd", "ef"]
        )

    def test_different_lengths_mixed(self):
        self.assertEqual(
            sorted_list_sum(["abcd", "ab", "abcdef", "xy"]),
            ["ab", "xy", "abcd", "abcdef"]
        )

    def test_case_sensitivity(self):
        self.assertEqual(
            sorted_list_sum(["AB", "ab", "CD", "cd"]),
            ["AB", "CD", "ab", "cd"]
        )

    # --- Edge Cases ---
    def test_single_even_string(self):
        self.assertEqual(
            sorted_list_sum(["ab"]),
            ["ab"]
        )

    def test_single_odd_string(self):
        self.assertEqual(
            sorted_list_sum(["abc"]),
            []
        )

    def test_empty_strings(self):
        self.assertEqual(
            sorted_list_sum(["", "", "a"]),
            ["", ""]
        )

    def test_very_long_strings(self):
        self.assertEqual(
            sorted_list_sum(["abcdefghij", "ab", "abcdefgh"]),
            ["ab", "abcdefgh", "abcdefghij"]
        )

    def test_numbers_as_strings(self):
        self.assertEqual(
            sorted_list_sum(["12", "123", "1234"]),
            ["12", "1234"]
        )

    def test_special_characters(self):
        self.assertEqual(
            sorted_list_sum(["!@", "#$", "%^&"]),
            ["!@", "#$"]
        )

    def test_mixed_alphanumeric(self):
        self.assertEqual(
            sorted_list_sum(["a1", "b2c", "d4"]),
            ["a1", "d4"]
        )

    # --- Boundary Cases ---
    def test_alphabetical_precedence(self):
        self.assertEqual(
            sorted_list_sum(["zz", "aa", "bb", "yy"]),
            ["aa", "bb", "yy", "zz"]
        )

    def test_length_precedence_over_alphabetical(self):
        self.assertEqual(
            sorted_list_sum(["zz", "aaaa", "bb"]),
            ["bb", "zz", "aaaa"]
        )

    def test_multiple_duplicates_different_lengths(self):
        self.assertEqual(
            sorted_list_sum(["ab", "abcd", "ab", "abcd", "ef"]),
            ["ab", "ab", "ef", "abcd", "abcd"]
        )

    def test_unicode_characters(self):
        self.assertEqual(
            sorted_list_sum(["αβ", "γδε", "ζη"]),
            ["αβ", "ζη"]
        )

    def test_whitespace_strings(self):
        self.assertEqual(
            sorted_list_sum(["  ", " ", "    "]),
            ["  ", "    "]
        )

    def test_mixed_whitespace_and_letters(self):
        self.assertEqual(
            sorted_list_sum([" a", "b ", "c d"]),
            [" a", "b ", "c d"]
        )

    # --- Invalid Input Tests ---
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            sorted_list_sum("not_a_list")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            sorted_list_sum(None)

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            sorted_list_sum([123, "ab"])

    def test_list_with_none_elements(self):
        with self.assertRaises(TypeError):
            sorted_list_sum([None, "ab"])

    def test_mixed_types_in_list(self):
        with self.assertRaises(TypeError):
            sorted_list_sum(["ab", 42, "cd"])

    def test_list_with_boolean_elements(self):
        with self.assertRaises(TypeError):
            sorted_list_sum([True, "ab", False])

if __name__ == '__main__':
    unittest.main()