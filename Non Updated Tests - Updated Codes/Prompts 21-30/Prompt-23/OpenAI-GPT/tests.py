# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import solve

class TestSolve(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solve(1000), "1")

    def test_example2(self):
        self.assertEqual(solve(150), "110")

    def test_example3(self):
        self.assertEqual(solve(147), "1100")

    def test_zero(self):
        self.assertEqual(solve(0), "0")

    def test_max_value(self):
        self.assertEqual(solve(9999), bin(36)[2:])  # 9+9+9+9 = 36 → "100100"

    def test_single_digit(self):
        self.assertEqual(solve(5), "101")

if __name__ == "__main__":
    unittest.main()
