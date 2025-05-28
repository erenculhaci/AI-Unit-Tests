# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    # --- Original Functional Tests ---
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

    # --- Additional Functional Tests ---
    def test_all_removed_palindrome(self):
        self.assertEqual(reverse_delete("abcba", "abc"), ("", True))

    def test_single_letter_palindrome(self):
        self.assertEqual(reverse_delete("x", ""), ("x", True))

    def test_single_letter_deleted(self):
        self.assertEqual(reverse_delete("x", "x"), ("", True))

    def test_spaces_and_punctuation(self):
        self.assertEqual(reverse_delete("a man a plan a canal panama", " "), ("amanaplanacanalpanama", True))

    def test_mixed_case_and_deletion(self):
        self.assertEqual(reverse_delete("RaceCar", "ae"), ("Rccr", False))

    def test_middle_deletion_palindrome(self):
        self.assertEqual(reverse_delete("racecar", "e"), ("raccar", False))

    def test_partial_palindrome(self):
        self.assertEqual(reverse_delete("radar", "r"), ("ada", True))

    def test_deletion_doesnt_affect_palindrome(self):
        self.assertEqual(reverse_delete("deified", "z"), ("deified", True))

    def test_deletion_breaks_palindrome(self):
        self.assertEqual(reverse_delete("deified", "d"), ("eifie", False))

    # --- Invalid Input Tests (Optional) ---
    def test_none_input(self):
        with self.assertRaises(TypeError):
            reverse_delete(None, "a")

    def test_numeric_input(self):
        with self.assertRaises(TypeError):
            reverse_delete(12321, "2")

    def test_list_input(self):
        with self.assertRaises(TypeError):
            reverse_delete(["a", "b", "c"], "b")

if __name__ == "__main__":
    unittest.main()
