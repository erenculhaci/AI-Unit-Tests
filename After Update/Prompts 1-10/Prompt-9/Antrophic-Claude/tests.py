# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import poly

class TestPolynomialFunction(unittest.TestCase):
    
    def test_constant_polynomial(self):
        """Test polynomial with just a constant term"""
        self.assertEqual(poly([5], 10), 5)
        self.assertEqual(poly([5], -10), 5)
    
    def test_linear_polynomial(self):
        """Test polynomial with constant and linear terms"""
        self.assertEqual(poly([2, 3], 1), 5)  # 2 + 3*1
        self.assertEqual(poly([2, 3], 2), 8)  # 2 + 3*2
        self.assertEqual(poly([2, 3], 0), 2)  # 2 + 3*0
    
    def test_quadratic_polynomial(self):
        """Test polynomial with constant, linear, and quadratic terms"""
        self.assertEqual(poly([1, 2, 3], 2), 17)  # 1 + 2*2 + 3*2^2
        self.assertEqual(poly([1, 2, 3], -1), 2)  # 1 + 2*(-1) + 3*(-1)^2
    
    def test_higher_degree_polynomial(self):
        """Test polynomial with higher degree terms"""
        self.assertEqual(poly([5, 4, 3, 2, 1], 2), 57)  # 5 + 4*2 + 3*2^2 + 2*2^3 + 1*2^4
    
    def test_zero_evaluation(self):
        """Test polynomial evaluated at x=0"""
        self.assertEqual(poly([7, 6, 5, 4], 0), 7)  # Only the constant term remains

if __name__ == '__main__':
    unittest.main()