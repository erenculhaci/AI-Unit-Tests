import unittest
from code import reverse_delete

class TestReverseDelete(unittest.TestCase):
    
    def test_example_1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
    
    def test_example_2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
    
    def test_example_3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))
    
    def test_empty_string(self):
        self.assertEqual(reverse_delete("", "abc"), ('', True))
    
    def test_empty_chars_to_delete(self):
        self.assertEqual(reverse_delete("abcba", ""), ('abcba', True))
    
    def test_delete_all_chars(self):
        self.assertEqual(reverse_delete("abc", "abc"), ('', True))
    
    def test_case_sensitivity(self):
        self.assertEqual(reverse_delete("AbCdE", "ae"), ('AbCd', False))
    
    def test_palindrome_after_deletion(self):
        self.assertEqual(reverse_delete("kitten", "ten"), ('ki', False))
        self.assertEqual(reverse_delete("racecar", "ae"), ('rccr', True))

if __name__ == '__main__':
    unittest.main()