import unittest
from code import find_zero

class TestFindZero(unittest.TestCase):
    def test_linear_polynomial(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)

    def test_cubic_polynomial(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

    def test_multiple_roots(self):
        result = find_zero([1, 0, -1, 0])  # x^3 - x = 0, roots at 0, 1, -1
        self.assertTrue(result in (-1.0, 0.0, 1.0))

    def test_invalid_coefficients_length(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

    def test_all_zero_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()