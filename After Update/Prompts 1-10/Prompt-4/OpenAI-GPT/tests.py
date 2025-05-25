# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import maximum

class TestMaximumFunction(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_example2(self):
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])

    def test_example3(self):
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_k_zero(self):
        self.assertEqual(maximum([1, 2, 3], 0), [])

    def test_duplicates(self):
        self.assertEqual(maximum([5, 5, 5, 1], 2), [5, 5])

    def test_all_elements(self):
        self.assertEqual(maximum([3, 1, 4, 1, 5], 5), [1, 1, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(maximum([], 0), [])

    def test_k_greater_than_length(self):
        self.assertEqual(maximum([1, 2, 3], 5), [1, 2, 3])

    def test_k_equals_length(self):
        self.assertEqual(maximum([9, 8, 7], 3), [7, 8, 9])

    def test_k_one(self):
        self.assertEqual(maximum([7, 6, 5, 4], 1), [7])

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            maximum([1, 2, 3], -1)

    def test_all_identical_elements(self):
        self.assertEqual(maximum([3, 3, 3, 3], 2), [3, 3])

    def test_all_negative(self):
        self.assertEqual(maximum([-5, -10, -3], 2), [-5, -3])

    def test_mixed_integers_and_floats(self):
        self.assertEqual(maximum([1.5, 2, 3.7, 3], 2), [3, 3.7])

    def test_all_floats(self):
        self.assertEqual(maximum([0.1, 0.2, 0.3, 0.4], 3), [0.2, 0.3, 0.4])

    def test_large_list(self):
        arr = list(range(10000))
        k = 5
        self.assertEqual(maximum(arr, k), [9995, 9996, 9997, 9998, 9999])

    def test_large_list_reverse(self):
        arr = list(range(10000, 0, -1))
        k = 5
        self.assertEqual(maximum(arr, k), [9996, 9997, 9998, 9999, 10000])

    def test_list_with_strings_should_fail(self):
        with self.assertRaises(TypeError):
            maximum([1, "a", 3], 2)

    def test_list_with_none_should_fail(self):
        with self.assertRaises(TypeError):
            maximum([1, None, 2], 2)

    def test_list_is_none(self):
        with self.assertRaises(TypeError):
            maximum(None, 2)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            maximum("12345", 3)

    def test_non_integer_k(self):
        with self.assertRaises(TypeError):
            maximum([1, 2, 3], "two")

    def test_float_k_should_fail(self):
        with self.assertRaises(TypeError):
            maximum([1, 2, 3], 2.5)

    def test_k_is_none(self):
        with self.assertRaises(TypeError):
            maximum([1, 2, 3], None)

    def test_tuple_input(self):
        self.assertEqual(maximum((5, 2, 9, 1), 2), [5, 9])

    def test_list_with_boolean_values(self):
        self.assertEqual(maximum([True, False, 1, 0], 2), [1, 1])

    def test_large_identical_values(self):
        self.assertEqual(maximum([999]*10000, 10), [999]*10)

if __name__ == "__main__":
    unittest.main()
