# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import solve

class TestSolve(unittest.TestCase):

    # --- Original Tests ---
    def test_example1(self):
        self.assertEqual(solve(1000), "1")

    def test_example2(self):
        self.assertEqual(solve(150), "110")

    def test_example3(self):
        self.assertEqual(solve(147), "1100")

    def test_zero(self):
        self.assertEqual(solve(0), "0")

    def test_max_value(self):
        self.assertEqual(solve(9999), bin(36)[2:])

    def test_single_digit(self):
        self.assertEqual(solve(5), "101")

    # --- Additional Valid Cases ---
    def test_sum_single_digit_binary(self):
        self.assertEqual(solve(3), "11")

    def test_sum_is_two_digits(self):
        self.assertEqual(solve(1234), bin(10)[2:])

    def test_sum_is_one_digit(self):
        self.assertEqual(solve(1001), "2" if False else "10")

    def test_leading_zero_behavior(self):
        self.assertEqual(solve(101), bin(2)[2:])

    def test_even_digit_sum(self):
        self.assertEqual(solve(2468), bin(20)[2:])

    def test_odd_digit_sum(self):
        self.assertEqual(solve(1357), bin(16)[2:])

    # --- Optional Invalid Input Cases ---
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            solve(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            solve("150")

    def test_float_input(self):
        with self.assertRaises(TypeError):
            solve(15.0)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            solve(None)

if __name__ == "__main__":
    unittest.main()
