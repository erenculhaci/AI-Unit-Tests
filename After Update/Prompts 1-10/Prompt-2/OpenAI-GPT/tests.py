# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import pluck

class TestPluckFunction(unittest.TestCase):
    
    # --- Basic functionality tests ---
    def test_example1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_example2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])

    def test_example3_empty(self):
        self.assertEqual(pluck([]), [])

    def test_example4_multiple_zeros(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_no_even_numbers(self):
        self.assertEqual(pluck([1, 3, 5, 7]), [])

    # --- Only one element ---
    def test_single_even_element(self):
        self.assertEqual(pluck([8]), [8, 0])

    def test_single_odd_element(self):
        self.assertEqual(pluck([9]), [])

    # --- All even elements ---
    def test_all_even_elements(self):
        self.assertEqual(pluck([6, 4, 2, 8]), [2, 2])

    # --- All odd elements ---
    def test_all_odd_elements(self):
        self.assertEqual(pluck([1, 3, 5]), [])

    # --- Same even number repeated ---
    def test_same_even_repeated(self):
        self.assertEqual(pluck([2, 2, 2]), [2, 0])

    # --- Mixed with same smallest even ---
    def test_multiple_same_smallest_even(self):
        self.assertEqual(pluck([7, 4, 2, 2, 4, 6]), [2, 2])

    # --- Negative even and odd numbers ---
    def test_negative_numbers(self):
        self.assertEqual(pluck([-2, -4, 3, 1]), [-4, 1])

    def test_mixed_negatives_and_positives(self):
        self.assertEqual(pluck([3, -2, 6, 0]), [-2, 1])

    # --- Large numbers ---
    def test_large_numbers(self):
        self.assertEqual(pluck([999999998, 1000000000, 2]), [2, 2])

    # --- Floats in list (should be ignored or raise error if strict) ---
    def test_list_with_floats(self):
        with self.assertRaises(TypeError):
            pluck([2.0, 4, 6])

    # --- Strings in list (invalid type) ---
    def test_list_with_strings(self):
        with self.assertRaises(TypeError):
            pluck([2, '4', 6])

    # --- Boolean in list ---
    def test_list_with_boolean(self):
        with self.assertRaises(TypeError):
            pluck([2, True, 4])

    # --- Nested lists ---
    def test_nested_lists(self):
        with self.assertRaises(TypeError):
            pluck([[2], 4, 6])

    # --- Non-list input ---
    def test_non_list_input_string(self):
        with self.assertRaises(TypeError):
            pluck("123")

    def test_non_list_input_integer(self):
        with self.assertRaises(TypeError):
            pluck(123)

    def test_non_list_input_none(self):
        with self.assertRaises(TypeError):
            pluck(None)

    def test_non_list_input_set(self):
        with self.assertRaises(TypeError):
            pluck({2, 4, 6})

    def test_non_list_input_dict(self):
        with self.assertRaises(TypeError):
            pluck({0: 2, 1: 4})

    # --- List with None inside ---
    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            pluck([1, None, 2])

    # --- Edge: very large input list ---
    def test_large_input_list(self):
        large_input = [1]*100000 + [2]
        self.assertEqual(pluck(large_input), [2, 100000])

    # --- Edge: smallest even value at index 0 ---
    def test_smallest_even_at_start(self):
        self.assertEqual(pluck([0, 2, 4, 6]), [0, 0])

if __name__ == '__main__':
    unittest.main()
