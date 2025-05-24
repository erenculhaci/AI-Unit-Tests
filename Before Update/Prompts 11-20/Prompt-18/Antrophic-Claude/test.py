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
        self.assertEqual(do_algebra(operators, operands), 9)  # ((2 + 3) * 4) - 5 = 9
    
    def test_all_operators(self):
        """Test using all supported operators."""
        operators = ['+', '-', '*', '//', '**']
        operands = [5, 3, 2, 4, 2, 3]
        # ((((5 + 3) - 2) * 4) // 2) ** 3 = 8 ** 3 = 512
        self.assertEqual(do_algebra(operators, operands), 512)
    
    def test_single_operator(self):
        """Test with just one operator."""
        operators = ['**']
        operands = [2, 3]
        self.assertEqual(do_algebra(operators, operands), 8)  # 2 ** 3 = 8
    
    def test_consecutive_same_operators(self):
        """Test with the same operator repeated."""
        operators = ['+', '+', '+']
        operands = [1, 2, 3, 4]
        self.assertEqual(do_algebra(operators, operands), 10)  # 1 + 2 + 3 + 4 = 10
    
    def test_floor_division(self):
        """Test with floor division to ensure it works correctly."""
        operators = ['//', '+', '//']
        operands = [10, 2, 3, 2]
        # ((10 // 2) + 3) // 2 = 8 // 2 = 4
        self.assertEqual(do_algebra(operators, operands), 4)

if __name__ == "__main__":
    unittest.main()