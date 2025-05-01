# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import do_algebra

class TestDoAlgebra(unittest.TestCase):
    def test_basic_operations(self):
        # Test with basic operations
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        self.assertEqual(do_algebra(operator, operand), 9)

    def test_exponentiation(self):
        # Test with exponentiation
        operator = ['**', '+']
        operand = [2, 3, 4]
        self.assertEqual(do_algebra(operator, operand), 12)

    def test_floor_division(self):
        # Test with floor division
        operator = ['//', '+']
        operand = [10, 3, 2]
        self.assertEqual(do_algebra(operator, operand), 5)

    def test_single_operator(self):
        # Test with a single operator
        operator = ['*']
        operand = [6, 7]
        self.assertEqual(do_algebra(operator, operand), 42)

    def test_invalid_operator(self):
        # Test with an invalid operator
        operator = ['+', '%']
        operand = [5, 3, 2]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

if __name__ == "__main__":
    unittest.main()