import unittest
from code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):
    
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

if __name__ == '__main__':
    unittest.main()