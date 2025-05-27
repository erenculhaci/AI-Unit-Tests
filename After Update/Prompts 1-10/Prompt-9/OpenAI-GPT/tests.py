# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import poly

class TestPolyComprehensive(unittest.TestCase):

    # --- VALID CASES ---

    def test_constant_only(self):
        self.assertEqual(poly([10], 5), 10)

    def test_zero_coefficients(self):
        self.assertEqual(poly([0, 0, 0, 0], 100), 0)

    def test_negative_x_value(self):
        self.assertEqual(poly([1, -1], -2), 1 + (-1)*(-2))  # 1 + 2 = 3

    def test_mixed_coefficients(self):
        self.assertEqual(poly([1, -2, 3, -4], 2), 1 + (-2)*2 + 3*4 + (-4)*8)  # 1 - 4 + 12 - 32 = -23

    def test_large_degree_polynomial(self):
        coeffs = [1] * 20
        x = 1
        self.assertEqual(poly(coeffs, x), 20)

    def test_large_x(self):
        self.assertEqual(poly([1, 2, 3], 1000), 1 + 2000 + 3000000)  # 3*10^6 + 2*10^3 + 1

    def test_float_coefficients(self):
        self.assertAlmostEqual(poly([1.5, -2.25, 3.125], 2), 1.5 + (-2.25)*2 + 3.125*4)

    def test_float_x(self):
        self.assertAlmostEqual(poly([2, 1], 0.5), 2 + 0.5)

    def test_high_precision_float_x(self):
        self.assertAlmostEqual(poly([0.1, 0.2, 0.3], 1.123456), 
                               0.1 + 0.2*1.123456 + 0.3*1.123456**2)

    def test_long_list_of_zeros(self):
        self.assertEqual(poly([0]*1000, 5), 0)

    def test_large_input_values(self):
        self.assertAlmostEqual(poly([1e10, -1e10, 1e10], 1e5), 1e10 - 1e15 + 1e20)

    # --- EDGE CASES ---

    def test_empty_coefficients_list(self):
        self.assertEqual(poly([], 5), 0)

    def test_empty_list_at_zero(self):
        self.assertEqual(poly([], 0), 0)

    def test_large_degree_and_large_x(self):
        result = poly([1] * 50, 2)  # Sum of 2^i from i=0 to 49: 2^50 - 1
        self.assertEqual(result, 2**50 - 1)

    def test_nan_and_inf_x(self):
        import math
        self.assertTrue(math.isnan(poly([1, 2], float('nan'))))
        self.assertEqual(poly([1], float('inf')), 1)
        self.assertTrue(math.isinf(poly([1, 1], float('inf'))))

    # --- INVALID INPUTS (TypeError expected) ---

    def test_none_input(self):
        with self.assertRaises(TypeError):
            poly(None, 1)

    def test_string_as_coefficients(self):
        with self.assertRaises(TypeError):
            poly(["a", "b", "c"], 1)

    def test_string_as_x(self):
        with self.assertRaises(TypeError):
            poly([1, 2, 3], "x")

    def test_nested_list(self):
        with self.assertRaises(TypeError):
            poly([[1, 2], [3, 4]], 1)

    def test_dict_input(self):
        with self.assertRaises(TypeError):
            poly({0: 1, 1: 2}, 2)

    def test_bool_input(self):
        self.assertEqual(poly([True, False, True], 2), 1 + 0 + 4)  # 5 (booleans as ints)

    def test_generator_input(self):
        with self.assertRaises(TypeError):
            poly((i for i in range(5)), 2)

    def test_tuple_input(self):
        self.assertEqual(poly((1, 2, 3), 2), 1 + 4 + 12)

    def test_none_inside_list(self):
        with self.assertRaises(TypeError):
            poly([1, None, 3], 2)

    def test_mixed_types_in_list(self):
        with self.assertRaises(TypeError):
            poly([1, "2", 3], 2)

    def test_complex_numbers(self):
        self.assertEqual(poly([1 + 2j, 3], 1), (1 + 2j) + 3*1)

    # --- SPECIAL CASES ---

    def test_large_float_precision(self):
        self.assertAlmostEqual(poly([1e-10, 1e-10, 1e-10], 1e10), 1e-10 + 1e0 + 1e10)

    def test_negative_power_behavior(self):
        self.assertEqual(poly([2, 3, 4], -2), 2 + 3*(-2) + 4*4)  # 2 - 6 + 16 = 12

    def test_huge_input_performance(self):
        coeffs = [1] * 100000  # 100k coefficients
        x = 1
        self.assertEqual(poly(coeffs, x), 100000)

if __name__ == "__main__":
    unittest.main()
