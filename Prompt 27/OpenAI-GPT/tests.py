import unittest
from code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

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

if __name__ == "__main__":
    unittest.main()
