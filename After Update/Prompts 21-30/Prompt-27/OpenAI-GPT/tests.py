# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    # --- Original Functional Tests ---
    def test_example1(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_example2(self):
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_example3(self):
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_short_word(self):
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_multiple_candidates(self):
        self.assertEqual(get_closest_vowel("crater"), "e")

    def test_consonant_edges(self):
        self.assertEqual(get_closest_vowel("plant"), "a")

    def test_no_vowel_between_consonants(self):
        self.assertEqual(get_closest_vowel("sky"), "")

    # --- Additional Functional Tests ---
    def test_uppercase_priority(self):
        self.assertEqual(get_closest_vowel("TRYING"), "I")

    def test_start_and_end_vowels_excluded(self):
        self.assertEqual(get_closest_vowel("angle"), "")  # 'a' and 'e' shouldn't count

    def test_multiple_vowels_between_consonants(self):
        self.assertEqual(get_closest_vowel("contraption"), "i")

    def test_last_valid_case(self):
        self.assertEqual(get_closest_vowel("scooter"), "e")

    def test_word_with_all_vowels(self):
        self.assertEqual(get_closest_vowel("educational"), "a")

    def test_closest_vowel_rightmost(self):
        self.assertEqual(get_closest_vowel("blockup"), "u")  # must pick 'u', not 'o'

    def test_vowel_alone_in_center(self):
        self.assertEqual(get_closest_vowel("bop"), "o")

    def test_all_vowels(self):
        self.assertEqual(get_closest_vowel("aeiou"), "")  # no consonants around vowels

    def test_all_consonants(self):
        self.assertEqual(get_closest_vowel("bcdfghjkl"), "")

    # --- Invalid Input Tests (Optional Robustness) ---
    def test_empty_string(self):
        self.assertEqual(get_closest_vowel(""), "")

    def test_one_letter(self):
        self.assertEqual(get_closest_vowel("a"), "")

    def test_two_letters(self):
        self.assertEqual(get_closest_vowel("at"), "")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(None)

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(123)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            get_closest_vowel(['a', 'b', 'c'])

if __name__ == "__main__":
    unittest.main()
