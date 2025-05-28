# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):
    
    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
    
    def test_example_2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")
    
    def test_empty_sentence(self):
        self.assertEqual(words_in_sentence(""), "")
    
    def test_single_word_prime_length(self):
        self.assertEqual(words_in_sentence("hello"), "hello")
        self.assertEqual(words_in_sentence("hi"), "hi")
        self.assertEqual(words_in_sentence("cat"), "cat")
    
    def test_single_word_non_prime_length(self):
        self.assertEqual(words_in_sentence("a"), "")
        self.assertEqual(words_in_sentence("four"), "")
        self.assertEqual(words_in_sentence("elephant"), "")
    
    def test_no_prime_length_words(self):
        self.assertEqual(words_in_sentence("a to do it"), "")
        self.assertEqual(words_in_sentence("four six eight"), "")
    
    def test_all_prime_length_words(self):
        self.assertEqual(words_in_sentence("hi the quick"), "hi the quick")
        self.assertEqual(words_in_sentence("go for seven"), "go for seven")
    
    def test_mixed_prime_non_prime(self):
        self.assertEqual(words_in_sentence("I am going home"), "am going")
        self.assertEqual(words_in_sentence("this test works fine"), "works")
    
    def test_prime_edge_cases(self):
        self.assertEqual(words_in_sentence("it go me"), "it go me")
        self.assertEqual(words_in_sentence("programming"), "programming")
        self.assertEqual(words_in_sentence("extraordinary"), "extraordinary")
    
    def test_multiple_spaces(self):
        self.assertEqual(words_in_sentence("hello  world   test"), "hello world")
        self.assertEqual(words_in_sentence("  go   for   it  "), "go for")
    
    def test_order_preservation(self):
        self.assertEqual(words_in_sentence("world hello test go"), "world hello go")
        self.assertEqual(words_in_sentence("zebra cat dog bird"), "cat dog bird")
    
    def test_case_sensitivity(self):
        self.assertEqual(words_in_sentence("Hello WORLD test"), "Hello WORLD")
        self.assertEqual(words_in_sentence("Go FOR it"), "Go FOR")
    
    def test_boundary_cases(self):
        self.assertEqual(words_in_sentence("a"), "")
        long_sentence = "hi the quick fox jumps over lazy dog again and again"
        expected = "hi the quick fox jumps over lazy dog again and again"
        self.assertEqual(words_in_sentence(long_sentence), expected)
    
    def test_same_length_words(self):
        self.assertEqual(words_in_sentence("cat dog pig"), "cat dog pig")
        self.assertEqual(words_in_sentence("four five nine"), "")
    
    # --- Invalid Input Tests ---
    def test_non_string_input_integer(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(123)
    
    def test_non_string_input_list(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(["hello", "world"])
    
    def test_non_string_input_none(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(None)
    
    def test_non_string_input_dict(self):
        with self.assertRaises(AttributeError):
            words_in_sentence({"key": "value"})
    
    def test_non_string_input_boolean(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(True)
    
    def test_non_string_input_float(self):
        with self.assertRaises(AttributeError):
            words_in_sentence(3.14)
    
    # --- Edge Cases for Prime Detection ---
    def test_prime_validation(self):
        self.assertEqual(words_in_sentence("a"), "")
        self.assertEqual(words_in_sentence("hi"), "hi")
        self.assertEqual(words_in_sentence("cat"), "cat")
        self.assertEqual(words_in_sentence("four"), "")
        self.assertEqual(words_in_sentence("hello"), "hello")
        self.assertEqual(words_in_sentence("python"), "")
        self.assertEqual(words_in_sentence("seventh"), "seventh")
    
    # --- Constraint Tests ---
    def test_numbers_in_words(self):
        self.assertEqual(words_in_sentence("hello123 world456"), "")
    
    def test_punctuation_in_words(self):
        self.assertEqual(words_in_sentence("hello, world!"), "")

if __name__ == "__main__":
    unittest.main()