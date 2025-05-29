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
        # 5 wells have water, so 5 total lowerings
        self.assertEqual(max_fill(grid, capacity), 5)
    
    def test_empty_grid(self):
        """Test with an empty grid."""
        grid = []
        capacity = 3
        self.assertEqual(max_fill(grid, capacity), 0)
    
    def test_single_cell_grid(self):
        """Test with a single cell grid."""
        grid = [[1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 1)
    
    def test_zero_capacity(self):
        """Test with zero capacity."""
        grid = [[1, 1], [0, 1]]
        capacity = 0
        # Can't remove any water with zero capacity
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)
    
    def test_negative_capacity(self):
        """Test with negative capacity (invalid input)."""
        grid = [[1, 0], [0, 1]]
        capacity = -2
        # Negative capacity should raise ValueError
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)
    
    def test_negative_water(self):
        """Test with negative water values (invalid input)."""
        grid = [[1, -1], [0, 1]]
        # Negative water values should raise ValueError
        capacity = 2
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)
    
    def test_non_integer_capacity(self):
        """Test with non-integer capacity (invalid input)."""
        grid = [[1, 0], [0, 1]]
        capacity = 2.5
        # Non-integer capacity should raise TypeError
        with self.assertRaises(TypeError):
            max_fill(grid, capacity)
    
    def test_uneven_rows(self):
        """Test with uneven row lengths (invalid grid structure)."""
        grid = [[1, 0, 1], [0, 1]]
        capacity = 2
        # Uneven rows should raise ValueError
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)
    
    def test_non_list_input(self):
        """Test with non-list input."""
        grid = "not a list"
        capacity = 2
        # Non-list input should raise TypeError
        with self.assertRaises(TypeError):
            max_fill(grid, capacity)
    
    def test_large_water_volumes(self):
        """Test with very large water volumes."""
        grid = [[100, 200], [300, 400]]
        capacity = 50
        # Each well requires ceil(water/capacity) lowerings
        # 100/50=2, 200/50=4, 300/50=6, 400/50=8
        # Total: 2+4+6+8=20 lowerings
        self.assertEqual(max_fill(grid, capacity), 20)
    
    def test_alternative_path(self):
        """Test with a grid where choosing suboptimal wells first would be incorrect."""
        grid = [[5, 0, 1], [0, 3, 0], [1, 0, 2]]
        capacity = 2
        # Optimal solution requires careful selection of wells
        # 5/2=3 (ceil), 3/2=2 (ceil), 2/2=1, 1/2=1 (ceil), 1/2=1 (ceil)
        # Total: 3+2+1+1+1=8 lowerings
        self.assertEqual(max_fill(grid, capacity), 8)

if __name__ == "__main__":
    unittest.main()