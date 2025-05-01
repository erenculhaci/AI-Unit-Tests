import unittest
from code import pluck

class TestPluck(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
        
    def test_only_one_even(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])
        
    def test_empty_array(self):
        self.assertEqual(pluck([]), [])
        
    def test_no_even_values(self):
        self.assertEqual(pluck([1, 3, 5, 7]), [])
        
    def test_multiple_same_smallest_even(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])
        
    def test_large_array(self):
        large_arr = [i for i in range(10000)]
        self.assertEqual(pluck(large_arr), [0, 0])
        
    def test_all_same_even_value(self):
        self.assertEqual(pluck([2, 2, 2, 2]), [2, 0])

if __name__ == "__main__":
    unittest.main()