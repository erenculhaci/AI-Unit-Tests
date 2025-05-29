# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):
    
    def test_example_1(self):
        """Test the first example from the problem statement"""
        self.assertEqual(
            sorted_list_sum(["aa", "a", "aaa"]),
            ["aa"]
        )
    
    def test_example_2(self):
        """Test the second example from the problem statement"""
        self.assertEqual(
            sorted_list_sum(["ab", "a", "aaa", "cd"]),
            ["ab", "cd"]
        )
    
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(
            sorted_list_sum([]),
            []
        )
    
    def test_no_even_length_strings(self):
        """Test with a list containing only odd length strings"""
        self.assertEqual(
            sorted_list_sum(["a", "abc", "abcde"]),
            []
        )
    
    def test_all_even_length_strings(self):
        """Test with a list containing only even length strings"""
        self.assertEqual(
            sorted_list_sum(["ab", "abcd", "abcdef"]),
            ["ab", "abcd", "abcdef"]
        )
    
    def test_mixed_length_strings(self):
        """Test with a list containing mixed odd and even length strings"""
        self.assertEqual(
            sorted_list_sum(["abcd", "a", "ab", "abc", "abcdef"]),
            ["ab", "abcd", "abcdef"]
        )
    
    def test_same_length_alphabetical_order(self):
        """Test sorting of same length strings alphabetically"""
        self.assertEqual(
            sorted_list_sum(["cd", "ab", "ef", "xy"]),
            ["ab", "cd", "ef", "xy"]
        )
    
    def test_duplicates(self):
        """Test with duplicate strings"""
        self.assertEqual(
            sorted_list_sum(["ab", "cd", "ab", "ef", "cd"]),
            ["ab", "ab", "cd", "cd", "ef"]
        )
    
    def test_different_lengths_mixed(self):
        """Test with strings of different even lengths"""
        self.assertEqual(
            sorted_list_sum(["abcd", "ab", "abcdef", "xy"]),
            ["ab", "xy", "abcd", "abcdef"]
        )
    
    def test_case_sensitivity(self):
        """Test that the sorting is case-sensitive"""
        self.assertEqual(
            sorted_list_sum(["AB", "ab", "CD", "cd"]),
            ["AB", "CD", "ab", "cd"]
        )

if __name__ == '__main__':
    unittest.main()