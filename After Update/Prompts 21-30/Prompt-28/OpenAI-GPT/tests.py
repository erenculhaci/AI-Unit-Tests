# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    # --- Valid Input Tests ---
    def test_basic_case(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")

    def test_power_of_two(self):
        self.assertEqual(decimal_to_binary(32), "db100000db")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_one(self):
        self.assertEqual(decimal_to_binary(1), "db1db")

    def test_large_number(self):
        self.assertEqual(decimal_to_binary(255), "db11111111db")

    def test_binary_padding_edge(self):
        self.assertEqual(decimal_to_binary(8), "db1000db")

    def test_multiple_bits_with_zeros(self):
        self.assertEqual(decimal_to_binary(18), "db10010db")

    def test_odd_number(self):
        self.assertEqual(decimal_to_binary(7), "db111db")

    def test_even_number(self):
        self.assertEqual(decimal_to_binary(10), "db1010db")

    def test_max_32bit_unsigned_int(self):
        self.assertEqual(decimal_to_binary(2**32 - 1), f"db{'1'*32}db")

    # --- Invalid Input Tests (Optional Robustness) ---
    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-1)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(3.14)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary("10")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(None)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary([10])

    def test_dict_input(self):
        with self.assertRaises(TypeError):
            decimal_to_binary({"number": 10})

if __name__ == "__main__":
    unittest.main()
