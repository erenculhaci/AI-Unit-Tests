# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import get_closest_vowel


class TestGetClosestVowel(unittest.TestCase):

    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_example_2(self):
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_example_3(self):
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_example_4(self):
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_multiple_vowels(self):
        self.assertEqual(get_closest_vowel("computer"), "e")

    def test_vowel_at_beginning(self):
        self.assertEqual(get_closest_vowel("apple"), "")

    def test_vowel_at_end(self):
        self.assertEqual(get_closest_vowel("taco"), "a")

    def test_no_vowels(self):
        self.assertEqual(get_closest_vowel("rhythm"), "")

    def test_case_sensitivity(self):
        self.assertEqual(get_closest_vowel("TeXt"), "e")

    def test_single_character(self):
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("b"), "")

    def test_two_characters(self):
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel("ae"), "")

    def test_three_characters_valid(self):
        self.assertEqual(get_closest_vowel("bat"), "a")
        self.assertEqual(get_closest_vowel("BET"), "E")

    def test_three_characters_invalid(self):
        self.assertEqual(get_closest_vowel("aei"), "")
        self.assertEqual(get_closest_vowel("xyz"), "")

    def test_vowel_at_edges(self):
        self.assertEqual(get_closest_vowel("elephant"), "a")
        self.assertEqual(get_closest_vowel("orange"), "a")

    def test_all_vowels(self):
        self.assertEqual(get_closest_vowel("aeiou"), "")

    def test_all_consonants(self):
        self.assertEqual(get_closest_vowel("bcdfg"), "")

    def test_rightmost_vowel_priority(self):
        self.assertEqual(get_closest_vowel("beautiful"), "u")
        self.assertEqual(get_closest_vowel("education"), "a")

    def test_mixed_case_complex(self):
        self.assertEqual(get_closest_vowel("ExAmPlE"), "A")
        self.assertEqual(get_closest_vowel("tEsT"), "E")

    def test_long_words(self):
        self.assertEqual(get_closest_vowel("programming"), "i")
        self.assertEqual(get_closest_vowel("extraordinary"), "a")

    def test_consecutive_vowels(self):
        self.assertEqual(get_closest_vowel("beautiful"), "u")
        self.assertEqual(get_closest_vowel("queue"), "")

    # --- Invalid Input Tests ---
    def test_non_string_input_integer(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(123)

    def test_non_string_input_list(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(["hello"])

    def test_non_string_input_none(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(None)

    def test_non_string_input_dict(self):
        with self.assertRaises(TypeError):
            get_closest_vowel({"word": "test"})

    def test_non_string_input_boolean(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(True)

    def test_non_string_input_float(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(3.14)

    # --- Edge Cases ---
    def test_empty_string(self):
        self.assertEqual(get_closest_vowel(""), "")

    def test_vowel_combinations(self):
        self.assertEqual(get_closest_vowel("bAe"), "")
        self.assertEqual(get_closest_vowel("cOd"), "O")
        self.assertEqual(get_closest_vowel("pIg"), "I")

    def test_pattern_validation(self):
        self.assertEqual(get_closest_vowel("strength"), "e")
        self.assertEqual(get_closest_vowel("system"), "e")


if __name__ == '__main__':
    unittest.main()
