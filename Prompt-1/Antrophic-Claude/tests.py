import unittest
from code import move_one_ball

class TestMoveOneBall(unittest.TestCase):
    
    def test_empty_array(self):
        """Test case for empty array"""
        self.assertTrue(move_one_ball([]), "Empty array should return True")
    
    def test_already_sorted(self):
        """Test case for already sorted array"""
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]), "Already sorted array should return True")
    
    def test_can_be_sorted(self):
        """Test case for array that can be sorted by right shifts"""
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]), "Array [3, 4, 5, 1, 2] should return True")
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4]), "Array [5, 1, 2, 3, 4] should return True")
    
    def test_cannot_be_sorted(self):
        """Test case for array that cannot be sorted by right shifts"""
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]), "Array [3, 5, 4, 1, 2] should return False")
        self.assertFalse(move_one_ball([2, 1, 4, 3]), "Array [2, 1, 4, 3] should return False")
    
    def test_single_element(self):
        """Test case for single element array"""
        self.assertTrue(move_one_ball([42]), "Single element array should return True")

if __name__ == '__main__':
    unittest.main()