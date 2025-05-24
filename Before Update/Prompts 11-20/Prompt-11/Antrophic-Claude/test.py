# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import max_fill

class TestMaxFill(unittest.TestCase):
    
    def test_example_1(self):
        """Test with the first example from the problem description."""
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)
    
    def test_example_2(self):
        """Test with the second example from the problem description."""
        grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)
    
    def test_example_3(self):
        """Test with the third example from the problem description."""
        grid = [[0, 0, 0], [0, 0, 0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)
    
    def test_full_grid(self):
        """Test with a grid where all cells contain water."""
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        capacity = 2
        # Each well has 3 units of water, needing 2 bucket operations (capacity=2)
        # 3 wells × 2 operations = 6 total lowerings
        self.assertEqual(max_fill(grid, capacity), 6)
    
    def test_large_capacity(self):
        """Test with a capacity larger than any well's water content."""
        grid = [[1, 0, 1], [0, 1, 1], [1, 0, 0]]
        capacity = 10
        # Each well with water needs only 1 lowering since capacity > water units
        # 3 wells have water, so 3 total lowerings
        self.assertEqual(max_fill(grid, capacity), 3)

if __name__ == "__main__":
    unittest.main()