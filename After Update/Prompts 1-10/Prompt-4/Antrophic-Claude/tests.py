# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
import code

class TestMaximumFunction(unittest.TestCase):
    
    def test_example_1(self):
        """Test with the first provided example"""
        arr = [-3, -4, 5]
        k = 3
        self.assertEqual(code.maximum(arr, k), [-4, -3, 5])
    
    def test_example_2(self):
        """Test with the second provided example"""
        arr = [4, -4, 4]
        k = 2
        self.assertEqual(code.maximum(arr, k), [4, 4])
    
    def test_example_3(self):
        """Test with the third provided example"""
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        self.assertEqual(code.maximum(arr, k), [2])
    
    def test_empty_result(self):
        """Test with k=0 which should return an empty list"""
        arr = [1, 2, 3, 4, 5]
        k = 0
        self.assertEqual(code.maximum(arr, k), [])
    
    def test_all_elements(self):
        """Test when k equals the length of the array"""
        arr = [3, 1, 4, 1, 5]
        k = 5
        self.assertEqual(code.maximum(arr, k), [1, 1, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()