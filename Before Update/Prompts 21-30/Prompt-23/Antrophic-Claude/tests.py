# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import solve

class TestSolve(unittest.TestCase):
    
    def test_example_1(self):
        self.assertEqual(solve(1000), "1")
    
    def test_example_2(self):
        self.assertEqual(solve(150), "110")
    
    def test_example_3(self):
        self.assertEqual(solve(147), "1100")
    
    def test_zero(self):
        self.assertEqual(solve(0), "0")
    
    def test_single_digit(self):
        self.assertEqual(solve(5), "101")
        self.assertEqual(solve(9), "1001")
    
    def test_large_number(self):
        self.assertEqual(solve(9999), "10110")  # Sum of digits is 36
    
    def test_boundary(self):
        self.assertEqual(solve(10000), "1")  # Sum of digits is 1
    
    def test_binary_power(self):
        self.assertEqual(solve(8), "1000")  # Sum of digits is 8

if __name__ == '__main__':
    unittest.main()