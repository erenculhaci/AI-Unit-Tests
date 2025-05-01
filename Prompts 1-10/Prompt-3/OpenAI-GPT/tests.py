import unittest
from code import minPath

class TestMinPath(unittest.TestCase):

    def test_example_1(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_example_2(self):
        grid = [
            [5, 9, 3],
            [4, 1, 6],
            [7, 8, 2]
        ]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_large_grid(self):
        grid = [
            [10, 3, 5, 1],
            [7, 14, 2, 8],
            [12, 13, 4, 9],
            [15, 11, 16, 6]
        ]
        k = 2
        expected = [1, 2]
        self.assertEqual(minPath(grid, k), expected)

    def test_grid_size_2(self):
        grid = [
            [2, 1],
            [3, 4]
        ]
        k = 4
        expected = [1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == '__main__':
    unittest.main()