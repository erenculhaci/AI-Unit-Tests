# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])

    def test_all_perfect(self):
        self.assertEqual(numerical_letter_grade([4.0, 4.0, 4.0]), ['A+', 'A+', 'A+'])

    def test_all_grade_boundaries(self):
        grades = [4.0, 3.71, 3.4, 3.05, 2.75, 2.4, 2.1, 1.8, 1.4, 1.1, 0.75, 0.1, 0.0]
        expected = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_exact_thresholds(self):
        grades = [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]
        expected = ['A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_floating_point_precision(self):
        grades = [3.70000001, 3.2999999, 2.0000001, 1.00000001, 0.69999999]
        expected = ['A', 'B+', 'C+', 'D+', 'D-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_duplicates(self):
        grades = [3.5, 3.5, 3.5, 3.5]
        expected = ['A-', 'A-', 'A-', 'A-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_empty_input(self):
        self.assertEqual(numerical_letter_grade([]), [])

    def test_minimum_and_maximum_values(self):
        grades = [0.0, 4.0]
        expected = ['E', 'A+']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_negative_and_above_max_values(self):
        with self.assertRaises(ValueError):
            numerical_letter_grade([-1.0])
        with self.assertRaises(ValueError):
            numerical_letter_grade([-0.1])
        with self.assertRaises(ValueError):
            numerical_letter_grade([4.1])
        with self.assertRaises(ValueError):
            numerical_letter_grade([10.0])

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            numerical_letter_grade(["A", None, {}, [], (3.0,)])

    def test_mixed_valid_and_invalid(self):
        with self.assertRaises(TypeError):
            numerical_letter_grade([3.5, "B", 2.0])

    def test_large_input_list(self):
        grades = [4.0] * 1000
        expected = ['A+'] * 1000
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_small_decimal_values(self):
        grades = [0.000001, 0.01, 0.2]
        expected = ['D-', 'D-', 'D-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_float_edge_precision_near_zero(self):
        grades = [0.0000001, 0.0]
        expected = ['D-', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_almost_exact_thresholds(self):
        epsilon = 1e-7
        grades = [
            3.7 - epsilon, 3.7, 3.7 + epsilon,
            3.3 - epsilon, 3.3, 3.3 + epsilon,
            2.0 - epsilon, 2.0, 2.0 + epsilon
        ]
        expected = [
            'A-', 'A-', 'A',
            'B+', 'B+', 'A-',
            'C', 'C', 'C+'
        ]
        self.assertEqual(numerical_letter_grade(grades), expected)

if __name__ == '__main__':
    unittest.main()