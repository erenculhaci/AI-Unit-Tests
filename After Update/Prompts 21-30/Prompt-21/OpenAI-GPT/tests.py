# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    # --- Original Functional Tests ---
    def test_single_even_length(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    def test_multiple_even_lengths(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_all_odd_lengths(self):
        self.assertEqual(sorted_list_sum(["a", "aaa", "abc"]), [])

    def test_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "bbb", "c"]), ["aa", "aa"])

    def test_sorting_order(self):
        self.assertEqual(sorted_list_sum(["dd", "cc", "aa", "bb"]), ["aa", "bb", "cc", "dd"])

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    # --- Additional Functional Tests ---
    def test_uppercase_sorting(self):
        self.assertEqual(sorted_list_sum(["aa", "AA", "Ab", "ba"]), ["AA", "Ab", "aa", "ba"])

    def test_same_length_mixed_case(self):
        self.assertEqual(sorted_list_sum(["zZ", "aa", "BB", "bB"]), ["BB", "aa", "bB", "zZ"])

    def test_only_even_length_words(self):
        self.assertEqual(sorted_list_sum(["hi", "to", "by"]), ["by", "hi", "to"])

    def test_long_even_length_words(self):
        self.assertEqual(sorted_list_sum(["python", "javaaa", "csharp", "aa"]), ["aa", "csharp", "javaaa", "python"])

    def test_empty_strings(self):
        self.assertEqual(sorted_list_sum(["", "a", "bb", "", "ccc"]), ["", ""])

    def test_special_characters(self):
        self.assertEqual(sorted_list_sum(["@@", "**", "!@#", "&*"]), ["**", "@@", "&*"])

    # --- Optional Robustness (if supported by implementation) ---
    def test_non_string_element(self):
        with self.assertRaises(TypeError):
            sorted_list_sum(["a", 123, "bb"])

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            sorted_list_sum(["a", None, "bb"])

if __name__ == "__main__":
    unittest.main()
