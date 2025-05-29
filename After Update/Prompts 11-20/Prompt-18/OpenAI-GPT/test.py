# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_example_from_docstring(self):
        """Test the example from the function's docstring."""
        operators = ['+', '*', '-']
        operands = [2, 3, 4, 5]
        self.assertEqual(do_algebra(operators, operands), 15)  # ((2 + 3) * 4) - 5 = 15

    def test_all_operators(self):
        """Test using all supported operators."""
        operators = ['+', '-', '*', '//', '**']
        operands = [5, 3, 2, 4, 2, 3]
        # ((((5 + 3) - 2) * 4) // 2) ** 3 = 1728
        self.assertEqual(do_algebra(operators, operands), 1728)

    def test_single_operator(self):
        operators = ['**']
        operands = [2, 3]
        self.assertEqual(do_algebra(operators, operands), 8)

    def test_consecutive_same_operators(self):
        operators = ['+', '+', '+']
        operands = [1, 2, 3, 4]
        self.assertEqual(do_algebra(operators, operands), 10)

    def test_floor_division(self):
        operators = ['//', '+', '//']
        operands = [10, 2, 3, 2]
        self.assertEqual(do_algebra(operators, operands), 4)

    def test_large_numbers(self):
        operators = ['**', '+']
        operands = [2, 10, 5000]
        self.assertEqual(do_algebra(operators, operands), 6024)

    def test_zero_division_error(self):
        operators = ['//']
        operands = [10, 0]
        with self.assertRaises(ZeroDivisionError):
            do_algebra(operators, operands)

    def test_zero_as_operand(self):
        operators = ['+', '*', '**']
        operands = [5, 0, 3, 2]
        self.assertEqual(do_algebra(operators, operands), 225)

    def test_operator_length_too_long(self):
        operators = ['+', '-', '*']
        operands = [1, 2, 3]
        with self.assertRaises(ValueError):
            do_algebra(operators, operands)

    def test_operator_length_too_short(self):
        operators = ['+']
        operands = [1, 2, 3, 4]
        with self.assertRaises(ValueError):
            do_algebra(operators, operands)

    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            do_algebra([], [])

    def test_minimum_valid_input(self):
        operators = ['+']
        operands = [1, 2]
        self.assertEqual(do_algebra(operators, operands), 3)

    def test_invalid_operator(self):
        operators = ['+', '%', '-']
        operands = [1, 2, 3, 4]
        with self.assertRaises(ValueError):
            do_algebra(operators, operands)

    def test_negative_result(self):
        operators = ['-', '*']
        operands = [5, 10, 3]
        self.assertEqual(do_algebra(operators, operands), -15)

    def test_complex_expression(self):
        operators = ['*', '**', '//', '+', '-']
        operands = [2, 3, 2, 5, 8, 10]
        self.assertEqual(do_algebra(operators, operands), 5)

if __name__ == "__main__":
    unittest.main()
