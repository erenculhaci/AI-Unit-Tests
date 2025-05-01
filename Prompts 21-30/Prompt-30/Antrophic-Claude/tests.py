import unittest
from code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):
    
    def test_example_1(self):
        """Test case for the first example in the prompt"""
        self.assertEqual(words_in_sentence("This is a test"), "is")
    
    def test_example_2(self):
        """Test case for the second example in the prompt"""
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")
    
    def test_empty_sentence(self):
        """Test case for an empty string"""
        self.assertEqual(words_in_sentence(""), "")
    
    def test_no_prime_length_words(self):
        """Test case where no words have prime lengths"""
        self.assertEqual(words_in_sentence("a to do"), "")
    
    def test_all_prime_length_words(self):
        """Test case where all words have prime lengths"""
        self.assertEqual(words_in_sentence("the quick brown"), "the quick brown")
        
    def test_with_punctuation(self):
        """Test case with punctuation (should count only letter length)"""
        self.assertEqual(words_in_sentence("hello, world!"), "hello, world!")
        
    def test_with_numbers(self):
        """Test case with numbers in words"""
        self.assertEqual(words_in_sentence("abc123 test"), "abc123")
        
    def test_single_character_words(self):
        """Test case with single character words (length 1 is not prime)"""
        self.assertEqual(words_in_sentence("a b c d"), "")

if __name__ == '__main__':
    unittest.main()