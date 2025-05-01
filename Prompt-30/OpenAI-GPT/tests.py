import unittest
from code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_empty(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_all_primes(self):
        self.assertEqual(words_in_sentence("hi you ate pie sun"), "hi you pie sun")

    def test_no_primes(self):
        self.assertEqual(words_in_sentence("wow good luck all day"), "")

if __name__ == "__main__":
    unittest.main()
