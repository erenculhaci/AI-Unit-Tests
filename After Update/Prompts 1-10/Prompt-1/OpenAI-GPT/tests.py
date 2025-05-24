# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    # --- Valid Functional Tests ---
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

    def test_decreasing_array(self):
        self.assertFalse(move_one_ball([5, 4, 3, 2, 1]))

    def test_two_elements_sorted(self):
        self.assertTrue(move_one_ball([1, 2]))

    def test_two_elements_unsorted(self):
        self.assertTrue(move_one_ball([2, 1]))

    def test_drop_at_end(self):
        self.assertTrue(move_one_ball([2, 3, 4, 5, 1]))

    def test_multiple_drops(self):
        self.assertFalse(move_one_ball([2, 4, 1, 5, 3]))

    def test_rotation_not_helpful(self):
        self.assertFalse(move_one_ball([1, 3, 2, 5, 4]))

    def test_large_valid_case(self):
        self.assertTrue(move_one_ball([6, 7, 8, 9, 1, 2, 3, 4, 5]))

    def test_large_invalid_case(self):
        self.assertFalse(move_one_ball([6, 7, 8, 2, 9, 1, 3, 4, 5]))

    def test_drop_in_middle(self):
        self.assertTrue(move_one_ball([4, 5, 1, 2, 3]))

    def test_no_drop_needed(self):
        self.assertTrue(move_one_ball([10]))

    def test_boundary_wrap(self):
        self.assertTrue(move_one_ball([9, 1, 2, 3, 4, 5, 6, 7, 8]))

    # --- Invalid Input Tests ---

    def test_non_list_input_integer(self):
        with self.assertRaises(TypeError):
            move_one_ball(123)

    def test_non_list_input_string(self):
        with self.assertRaises(TypeError):
            move_one_ball("12345")

    def test_non_list_input_none(self):
        with self.assertRaises(TypeError):
            move_one_ball(None)

    def test_list_with_string_elements(self):
        with self.assertRaises(TypeError):
            move_one_ball(["a", "b", "c"])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            move_one_ball([1, "2", 3])

    def test_list_with_nested_list(self):
        with self.assertRaises(TypeError):
            move_one_ball([1, [2], 3])

    def test_list_with_dict_element(self):
        with self.assertRaises(TypeError):
            move_one_ball([1, {"key": 2}, 3])

    def test_list_with_boolean_values(self):
        with self.assertRaises(TypeError):
            move_one_ball([True, False, 1])

    def test_list_with_float_values(self):
        with self.assertRaises(TypeError):
            move_one_ball([1.0, 2.5, 3.1])

if __name__ == "__main__":
    unittest.main()
