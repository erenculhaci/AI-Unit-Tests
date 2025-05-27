# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import find_zero
import math


class TestFindZero(unittest.TestCase):

    def test_linear_polynomial(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=10)
        self.assertAlmostEqual(find_zero([-3, 6]), 0.5, places=10)

    def test_cubic_polynomial(self):
        result = find_zero([-6, 11, -6, 1])
        self.assertIn(round(result, 10), [1.0, 2.0, 3.0])

    def test_higher_degree_polynomial(self):
        # f(x) = x(x^2 - 1)(x^2 - 4) = x^5 - 5x^3 + 4x
        result = find_zero([0, 4, 0, -5, 0, 1])
        self.assertIn(round(result, 10), [-2.0, -1.0, 0.0, 1.0, 2.0])

    def test_even_coefficient_requirement(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])  # odd number of coefficients

    def test_all_zero_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([0, 0, 0, 0])

    def test_zero_leading_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 0, 0])  # Last coefficients zero, not a proper polynomial

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            find_zero([1, 'a', 3.5, 2])

    def test_non_list_input(self):
        with self.assertRaises(AttributeError):
            find_zero("x^2 + 1")

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_zero([])

    def test_duplicate_real_roots(self):
        # f(x) = (x - 2)^2 (x + 1) -> roots: 2 (multiplicity 2), -1
        result = find_zero([4, 0, -3, 1])
        self.assertAlmostEqual(result, 2.0, places=6)

    def test_close_roots(self):
        # f(x) = (x - 1e-6)(x - 2e-6)(x - 3e-6)
        coeffs = [-6e-18, 1.1e-11, -6e-6, 1]
        result = find_zero(coeffs)
        self.assertTrue(
            math.isclose(result, 1e-6, rel_tol=1e-2) or
            math.isclose(result, 2e-6, rel_tol=1e-2) or
            math.isclose(result, 3e-6, rel_tol=1e-2)
        )

    def test_large_coefficients(self):
        # f(x) = 1e10 * x - 1e5, root at x = 1e-5
        result = find_zero([-1e5, 1e10])
        self.assertAlmostEqual(result, 1e-5, places=5)

    def test_small_coefficients(self):
        # f(x) = 1e-10 * x + 1e-5, root at x = -1e5
        result = find_zero([1e-5, 1e-10])
        self.assertAlmostEqual(result, -1e5, places=2)

    def test_root_at_zero(self):
        # f(x) = x * (x - 1)^2 = x^3 - 2x^2 + x
        result = find_zero([0, 1, -2, 1])
        self.assertIn(round(result, 10), [0.0, 1.0])

    def test_high_degree_polynomial(self):
        # f(x) = x^7 - x^5 = x^5 (x^2 - 1), roots: 0, 1, -1
        result = find_zero([0, 0, 0, 0, 0, -1, 0, 1])
        self.assertIn(round(result, 10), [-1.0, 0.0, 1.0])

    def test_no_real_roots(self):
        # f(x) = x^2 + 1 -> no real roots
        with self.assertRaises(ValueError): #this will raise ValueError since even number of coefficients raise ValueError
            find_zero([1, 0, 1])

    def test_polynomial_with_many_zero_coefficients(self):
        # f(x) = x^7 - 1, with zeros in between
        result = find_zero([-1, 0, 0, 0, 0, 0, 0, 1])
        self.assertIn(round(result, 10), [-1.0, 1.0])


    def test_multiple_valid_roots_precision(self):
        # f(x) = x(x - sqrt(2))(x + sqrt(2)) = x^3 - 2x
        result = find_zero([0, -2, 0, 1])
        self.assertTrue(
            math.isclose(result, math.sqrt(2), rel_tol=1e-5) or 
            math.isclose(result, -math.sqrt(2), rel_tol=1e-5) or
            math.isclose(result, 0.0, rel_tol=1e-5)
        )

    def test_large_degree_even_length_polynomial(self):
        # f(x) = x^9 - x = x(x^2 - 1)(x^6 + ...), roots include 0, 1, -1
        result = find_zero([0, -1, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertIn(round(result, 10), [-1.0, 0.0, 1.0])


    def test_inf_nan_values(self):
        import math
        with self.assertRaises(TypeError):
            find_zero([1, math.nan])
        with self.assertRaises(TypeError):
            find_zero([1, math.inf])

    def test_boolean_input_in_coefficients(self):
        # raise value error if boolean input is given
        with self.assertRaises(ValueError):
            find_zero([1, True, 3.5, False])

    def test_find_zero_with_rounding(self):
        self.assertEqual(round(find_zero([1, 2]), 2), -0.5)


if __name__ == '__main__':
    unittest.main()
