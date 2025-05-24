# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import poly

class TestPoly(unittest.TestCase):

    def test_single_coefficient(self):
        self.assertEqual(poly([5], 10), 5)

    def test_linear_polynomial(self):
        self.assertEqual(poly([2, 3], 4), 2 + 3 * 4)  # 2 + 12 = 14

    def test_quadratic_polynomial(self):
        self.assertEqual(poly([1, 0, 2], 2), 1 + 0*2 + 2*(2**2))  # 1 + 0 + 8 = 9

    def test_zero_polynomial(self):
        self.assertEqual(poly([0, 0, 0], 5), 0)

    def test_negative_coefficients(self):
        self.assertEqual(poly([-1, -2, -3], 2), -1 + (-2)*2 + (-3)*(2**2))  # -1 - 4 - 12 = -17

if __name__ == "__main__":
    unittest.main()
