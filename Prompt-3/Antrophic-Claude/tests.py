import unittest
from code import minPath

class TestMinPath(unittest.TestCase):
    def test_example1(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_example2(self):
        grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_larger_grid(self):
        grid = [
            [1, 16, 5, 14],
            [4, 7, 12, 15],
            [8, 11, 10, 13],
            [2, 3, 6, 9]
        ]
        k = 4
        expected = [1, 4, 8, 2]  # This should be the minimum path of length 4
        self.assertEqual(minPath(grid, k), expected)
    
    def test_longer_path(self):
        grid = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        k = 5
        expected = [1, 2, 3, 4, 3]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_two_by_two_grid(self):
        grid = [[1, 3], [4, 2]]
        k = 3
        expected = [1, 4, 1]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == "__main__":
    unittest.main()