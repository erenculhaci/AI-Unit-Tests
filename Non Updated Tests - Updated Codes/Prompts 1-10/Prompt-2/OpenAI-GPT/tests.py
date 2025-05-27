# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import pluck

class TestPluckFunction(unittest.TestCase):
    
    def test_example1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_example2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])

    def test_example3_empty(self):
        self.assertEqual(pluck([]), [])

    def test_example4_multiple_zeros(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_no_even_numbers(self):
        self.assertEqual(pluck([1, 3, 5, 7]), [])

if __name__ == '__main__':
    unittest.main()
