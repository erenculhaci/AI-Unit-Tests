# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import minPath

class TestMinPath(unittest.TestCase):
    def test_small_grid_k1(self):
        grid = [
            [4, 2],
            [3, 1]
        ]
        expected = [1]
        result = minPath(grid, 1)
        self.assertEqual(result, expected)

    def test_small_grid_k2(self):
        grid = [
            [4, 2],
            [3, 1]
        ]
        expected = [1, 2]
        result = minPath(grid, 2)
        self.assertEqual(result, expected)

    def test_small_grid_k3(self):
        grid = [
            [4, 2],
            [3, 1]
        ]
        expected = [1, 2, 4]
        result = minPath(grid, 3)
        self.assertEqual(result, expected)

    def test_k_equal_1_in_larger_grid(self):
        grid = [
            [5, 3, 9],
            [1, 8, 7],
            [4, 6, 2]
        ]
        expected = [1]
        result = minPath(grid, 1)
        self.assertEqual(result, expected)

    def test_k_longer_path(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = 4
        result = minPath(grid, k)
        self.assertEqual(len(result), k)
        for i in range(1, len(result)):
            self.assertTrue(result[i] >= result[i-1])

    def test_k_greater_than_max_path(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 5
        result = minPath(grid, k)
        self.assertEqual(result, [])

    def test_k_zero(self):
        grid = [[1]]
        result = minPath(grid, 0)
        self.assertEqual(result, [])

    def test_k_negative(self):
        grid = [[1]]
        result = minPath(grid, -3)
        self.assertEqual(result, [])

    def test_single_cell_grid_k1(self):
        grid = [[42]]
        expected = [42]
        result = minPath(grid, 1)
        self.assertEqual(result, expected)

    def test_single_cell_grid_k_greater_than_1(self):
        grid = [[42]]
        k = 2
        result = minPath(grid, k)
        self.assertEqual(result, [])

    def test_path_adjacency(self):
        grid = [
            [1, 2, 3],
            [6, 5, 4],
            [7, 8, 9]
        ]
        k = 4
        result = minPath(grid, k)
        pos = {val: (i, j) for i, row in enumerate(grid) for j, val in enumerate(row)}
        for i in range(1, len(result)):
            x1, y1 = pos[result[i-1]]
            x2, y2 = pos[result[i]]
            self.assertTrue(abs(x1 - x2) + abs(y1 - y2) == 1)

    def test_lex_ordering_check(self):
        grid = [
            [10, 1],
            [2, 9]
        ]
        k = 2
        expected = [1, 9]
        result = minPath(grid, k)
        self.assertEqual(result, expected)

    def test_duplicate_values_grid(self):
        grid = [
            [1, 1],
            [2, 2]
        ]
        k = 2
        result = minPath(grid, k)
        self.assertIsInstance(result, list)

    def test_larger_grid_performance(self):
        n = 5
        grid = [list(range(i * n + 1, i * n + n + 1)) for i in range(n)]
        k = 7
        result = minPath(grid, k)
        self.assertEqual(len(result), k)

    def test_path_length_matches_k(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 3
        result = minPath(grid, k)
        self.assertEqual(len(result), k)

    def test_non_square_grid_behavior(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        try:
            result = minPath(grid, 2)
            self.assertIsInstance(result, list)
        except Exception:
            pass

    def test_grid_contains_strings(self):
        grid = [
            [1, 'a'],
            [2, 3]
        ]
        k = 2
        with self.assertRaises(TypeError):
            minPath(grid, k)

    def test_grid_contains_none(self):
        grid = [
            [None, 2],
            [3, 4]
        ]
        k = 2
        with self.assertRaises(TypeError):
            minPath(grid, k)

    def test_grid_contains_floats(self):
        grid = [
            [1.1, 2.2],
            [3.3, 4.4]
        ]
        k = 2
        with self.assertRaises(TypeError):
            minPath(grid, k)

    def test_k_is_string(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = "3"
        with self.assertRaises(TypeError):
            minPath(grid, k)

    def test_k_is_float(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 3.5
        with self.assertRaises(TypeError):
            minPath(grid, k)

    def test_grid_is_not_list(self):
        grid = "not a list"
        k = 2
        with self.assertRaises(TypeError):
            minPath(grid, k)

    def test_grid_rows_are_not_lists(self):
        grid = [1, 2, 3, 4]
        k = 2
        with self.assertRaises(TypeError):
            minPath(grid, k)

    def test_empty_grid(self):
        grid = []
        k = 1
        result = minPath(grid, k)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
