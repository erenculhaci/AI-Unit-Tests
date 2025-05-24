# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ("bcd", False))

    def test_example2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ("acdef", False))

    def test_example3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ("cdedc", True))

    def test_empty_string(self):
        self.assertEqual(reverse_delete("", "aeiou"), ("", True))

    def test_delete_all(self):
        self.assertEqual(reverse_delete("aeiou", "aeiou"), ("", True))

    def test_no_deletions(self):
        self.assertEqual(reverse_delete("madam", ""), ("madam", True))

    def test_case_sensitive(self):
        self.assertEqual(reverse_delete("MadAm", "a"), ("MdAm", False))

if __name__ == "__main__":
    unittest.main()
