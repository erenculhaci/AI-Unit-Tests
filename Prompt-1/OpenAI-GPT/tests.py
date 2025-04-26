import unittest
from code import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    def test_sorted_after_shift(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_not_possible_to_sort(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_already_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([42]))

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

if __name__ == "__main__":
    unittest.main()
