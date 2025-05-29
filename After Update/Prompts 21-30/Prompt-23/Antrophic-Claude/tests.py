# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import solve


class TestSolve(unittest.TestCase):

    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(solve(1000), "1")

    def test_example_2(self):
        self.assertEqual(solve(150), "110")

    def test_example_3(self):
        self.assertEqual(solve(147), "1100")

    def test_zero(self):
        self.assertEqual(solve(0), "0")

    def test_single_digit(self):
        self.assertEqual(solve(5), "101")
        self.assertEqual(solve(9), "1001")
        self.assertEqual(solve(1), "1")
        self.assertEqual(solve(2), "10")

    def test_large_number(self):
        self.assertEqual(solve(9999), "100100")

    def test_boundary(self):
        self.assertEqual(solve(10000), "1")

    def test_binary_power(self):
        self.assertEqual(solve(8), "1000")

    def test_two_digit_numbers(self):
        self.assertEqual(solve(10), "1")
        self.assertEqual(solve(99), "10010")
        self.assertEqual(solve(11), "10")
        self.assertEqual(solve(23), "101")

    def test_three_digit_numbers(self):
        self.assertEqual(solve(123), "110")
        self.assertEqual(solve(456), "1111")
        self.assertEqual(solve(789), "11000")

    def test_four_digit_numbers(self):
        self.assertEqual(solve(1234), "1010")
        self.assertEqual(solve(5678), "11010")
        self.assertEqual(solve(1111), "100")

    def test_numbers_with_zeros(self):
        self.assertEqual(solve(101), "10")
        self.assertEqual(solve(1001), "10")
        self.assertEqual(solve(5005), "1010")

    def test_repeated_digits(self):
        self.assertEqual(solve(2222), "1000")
        self.assertEqual(solve(3333), "1100")
        self.assertEqual(solve(7777), "11100")

    def test_mixed_patterns(self):
        self.assertEqual(solve(1357), "10000")
        self.assertEqual(solve(2468), "10100")
        self.assertEqual(solve(1919), "10100")

    def test_edge_constraint_values(self):
        self.assertEqual(solve(0), "0")
        self.assertEqual(solve(10000), "1")
        self.assertEqual(solve(9876), "11110")

    # --- Invalid Input Tests ---
    def test_non_integer_input_string(self):
        with self.assertRaises(TypeError):
            solve("123")

    def test_non_integer_input_float(self):
        with self.assertRaises(TypeError):
            solve(123.45)

    def test_non_integer_input_list(self):
        with self.assertRaises(TypeError):
            solve([1, 2, 3])

    def test_non_integer_input_none(self):
        with self.assertRaises(TypeError):
            solve(None)

    def test_non_integer_input_dict(self):
        with self.assertRaises(TypeError):
            solve({"number": 123})

    def test_non_integer_input_boolean(self):
        with self.assertRaises(TypeError):
            solve(True)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            solve(-1)

    def test_out_of_range_input(self):
        with self.assertRaises(ValueError):
            solve(10001)

    # --- Edge Cases ---
    def test_binary_representation_validation(self):
        self.assertEqual(solve(15), "110")
        self.assertEqual(solve(31), "100")
        self.assertEqual(solve(63), "1001")

    def test_maximum_digit_sum(self):
        self.assertEqual(solve(9999), "100100")

    def test_minimum_digit_sum(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(2000), "10")
        self.assertEqual(solve(3000), "11")


if __name__ == '__main__':
    unittest.main()
