# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

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

if __name__ == "__main__":
    unittest.main()
