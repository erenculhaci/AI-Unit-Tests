# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import max_fill

class TestMaxFill(unittest.TestCase):
    def test_case_1(self):
        # Example 1: Normal case
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_case_2(self):
        # Example 2: Larger grid with mixed values
        grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)

    def test_case_3(self):
        # Example 3: Empty grid
        grid = [[0, 0, 0], [0, 0, 0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_case_4(self):
        # Edge case: Single row with maximum water
        grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        capacity = 3
        self.assertEqual(max_fill(grid, capacity), 4)

    def test_case_5(self):
        # Edge case: Single cell with water
        grid = [[7]]
        capacity = 3
        self.assertEqual(max_fill(grid, capacity), 3)

if __name__ == "__main__":
    unittest.main()