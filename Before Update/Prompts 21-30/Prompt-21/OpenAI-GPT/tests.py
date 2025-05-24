# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_single_even_length(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    def test_multiple_even_lengths(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_all_odd_lengths(self):
        self.assertEqual(sorted_list_sum(["a", "aaa", "abc"]), [])

    def test_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "bbb", "c"]), ["aa", "aa"])

    def test_sorting_order(self):
        self.assertEqual(sorted_list_sum(["dd", "cc", "aa", "bb"]), ["aa", "bb", "cc", "dd"])

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

if __name__ == "__main__":
    unittest.main()
