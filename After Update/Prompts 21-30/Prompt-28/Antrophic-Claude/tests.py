# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import decimal_to_binary


class TestDecimalToBinary(unittest.TestCase):

    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")

    def test_example_2(self):
        self.assertEqual(decimal_to_binary(32), "db100000db")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_one(self):
        self.assertEqual(decimal_to_binary(1), "db1db")

    def test_small_numbers(self):
        self.assertEqual(decimal_to_binary(2), "db10db")
        self.assertEqual(decimal_to_binary(3), "db11db")
        self.assertEqual(decimal_to_binary(4), "db100db")
        self.assertEqual(decimal_to_binary(7), "db111db")

    def test_powers_of_two(self):
        self.assertEqual(decimal_to_binary(8), "db1000db")
        self.assertEqual(decimal_to_binary(16), "db10000db")
        self.assertEqual(decimal_to_binary(64), "db1000000db")
        self.assertEqual(decimal_to_binary(128), "db10000000db")

    def test_large_numbers(self):
        self.assertEqual(decimal_to_binary(255), "db11111111db")
        self.assertEqual(decimal_to_binary(1024), "db10000000000db")
        self.assertEqual(decimal_to_binary(123), "db1111011db")

    def test_random_numbers(self):
        self.assertEqual(decimal_to_binary(10), "db1010db")
        self.assertEqual(decimal_to_binary(42), "db101010db")
        self.assertEqual(decimal_to_binary(100), "db1100100db")
        self.assertEqual(decimal_to_binary(200), "db11001000db")

    def test_edge_cases(self):
        self.assertEqual(decimal_to_binary(31), "db11111db")
        self.assertEqual(decimal_to_binary(63), "db111111db")
        self.assertEqual(decimal_to_binary(127), "db1111111db")

    def test_format_verification(self):
        result = decimal_to_binary(15)
        self.assertTrue(result.startswith("db"))
        self.assertTrue(result.endswith("db"))
        self.assertEqual(len(result), 8)

    def test_binary_content_verification(self):
        result = decimal_to_binary(42)
        middle_part = result[2:-2]
        for char in middle_part:
            self.assertIn(char, ['0', '1'])

    # --- Invalid Input Tests ---
    def test_negative_number(self):
        with self.assertRaises((ValueError, OverflowError)):
            decimal_to_binary(-1)

    def test_non_integer_input_float(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(3.14)

    def test_non_integer_input_string(self):
        with self.assertRaises(TypeError):
            decimal_to_binary("123")

    def test_non_integer_input_none(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(None)

    def test_non_integer_input_list(self):
        with self.assertRaises(TypeError):
            decimal_to_binary([1, 2, 3])

    def test_non_integer_input_dict(self):
        with self.assertRaises(TypeError):
            decimal_to_binary({"key": "value"})

    # --- Edge Cases for Binary Conversion ---
    def test_very_large_numbers(self):
        self.assertEqual(decimal_to_binary(1023), "db1111111111db")
        self.assertEqual(decimal_to_binary(2047), "db11111111111db")

    def test_consecutive_numbers(self):
        self.assertEqual(decimal_to_binary(5), "db101db")
        self.assertEqual(decimal_to_binary(6), "db110db")
        self.assertEqual(decimal_to_binary(9), "db1001db")

    def test_boundary_values(self):
        self.assertEqual(decimal_to_binary(511), "db111111111db")
        self.assertEqual(decimal_to_binary(512), "db1000000000db")


if __name__ == "__main__":
    unittest.main()