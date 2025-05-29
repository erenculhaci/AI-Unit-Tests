# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import get_row

class TestGetRow(unittest.TestCase):
    
    def test_example_from_docstring(self):
        lst = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ]
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        self.assertEqual(get_row(lst, 1), expected)
    
    def test_empty_input(self):
        self.assertEqual(get_row([], 1), [])
    
    def test_with_empty_rows(self):
        lst = [[], [1], [1, 2, 3]]
        self.assertEqual(get_row(lst, 3), [(2, 2)])
    
    def test_no_occurrences(self):
        lst = [
            [2, 3, 4],
            [5, 6, 7],
            [8, 9, 10]
        ]
        self.assertEqual(get_row(lst, 1), [])
        
    def test_none_input(self):
        with self.assertRaises(TypeError):
            get_row(None, 1)
            
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            get_row("not a list", 1)
            
    def test_non_integer_target(self):
        lst = [[1, 2], [3, 4]]
        with self.assertRaises(TypeError):
            get_row(lst, "1")
        
    def test_mixed_type_values(self):
        lst = [
            [1, "2", 3],
            [4, 5, "1"]
        ]
        self.assertEqual(get_row(lst, 1), [(0, 0)])
        
    def test_negative_target(self):
        lst = [
            [-1, 2, 3],
            [4, -1, 6]
        ]
        expected = [(0, 0), (1, 1)]
        self.assertEqual(get_row(lst, -1), expected)
        
    def test_zero_target(self):
        lst = [
            [0, 1, 2],
            [3, 0, 0]
        ]
        expected = [(0, 0), (1, 2), (1, 1)]
        self.assertEqual(get_row(lst, 0), expected)
        
    def test_nested_lists(self):
        lst = [
            [[1, 2], 3],
            [4, [5, 1]]
        ]
        with self.assertRaises(TypeError):
            get_row(lst, 1)
        

        
    def test_duplicate_coordinates(self):
        lst = [
            [1, 2, 3],
            [1, 1, 1]
        ]
        expected = [(0, 0), (1, 2), (1, 1), (1, 0)]
        self.assertEqual(get_row(lst, 1), expected)

if __name__ == "__main__":
    unittest.main()
