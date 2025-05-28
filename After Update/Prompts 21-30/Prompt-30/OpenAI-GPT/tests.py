# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    # --- Functional Tests from Original Examples ---
    def test_example1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    # --- Additional Functional Tests ---
    def test_empty(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_all_primes(self):
        self.assertEqual(words_in_sentence("hi you ate pie sun"), "hi you pie sun")

    def test_no_primes(self):
        self.assertEqual(words_in_sentence("wow good luck all day"), "")

    def test_single_word_prime_length(self):
        self.assertEqual(words_in_sentence("hey"), "hey")

    def test_single_word_nonprime_length(self):
        self.assertEqual(words_in_sentence("four"), "")

    def test_mixed_length_words(self):
        self.assertEqual(words_in_sentence("yes I can see why not"), "yes I can")

    def test_all_two_letter_words(self):
        self.assertEqual(words_in_sentence("an is it me up go by"), "an is it me up go by")

    def test_mixed_case_sentence(self):
        self.assertEqual(words_in_sentence("Hello world I am AI"), "I am AI")

    def test_long_sentence(self):
        sentence = "The quick brown fox jumps over the lazy dog again tomorrow"
        self.assertEqual(words_in_sentence(sentence), "The over dog")

    def test_boundary_prime_lengths(self):
        self.assertEqual(words_in_sentence("a ab abc abcd abcde abcdef abcdefg"), "ab abc abcde abcdefg")

    # --- Invalid Input Tests
    def test_none_input(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(None)

    def test_integer_input(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(123)

    def test_list_input(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(["this", "is", "not", "a", "string"])

if __name__ == "__main__":
    unittest.main()
