# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import intersection

class TestIntersection(unittest.TestCase):

    # --- Functional Tests from Original Examples ---
    def test_no_intersection_at_point(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_partial_overlap(self):
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")

    def test_full_overlap_prime(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_partial_overlap_non_prime(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_no_overlap(self):
        self.assertEqual(intersection((5, 6), (7, 8)), "NO")

    def test_intersection_length_two(self):
        self.assertEqual(intersection((1, 4), (3, 5)), "YES")

    def test_same_interval(self):
        self.assertEqual(intersection((2, 5), (2, 5)), "NO")

    # --- Additional Functional Tests ---
    def test_single_point_intersection(self):
        self.assertEqual(intersection((0, 0), (0, 0)), "NO")

    def test_full_overlap_even_length(self):
        self.assertEqual(intersection((1, 6), (2, 5)), "NO")

    def test_full_overlap_length_three(self):
        self.assertEqual(intersection((1, 5), (2, 4)), "YES")

    def test_negative_intervals_with_prime_length(self):
        self.assertEqual(intersection((-10, -6), (-8, -4)), "YES")

    def test_large_intervals_non_prime(self):
        self.assertEqual(intersection((0, 100), (50, 160)), "NO")

    def test_large_intervals_prime(self):
        self.assertEqual(intersection((0, 100), (50, 152)), "YES")
        self.assertEqual(intersection((0, 100), (50, 150)), "NO")

    def test_overlap_length_seven(self):
        self.assertEqual(intersection((10, 20), (14, 20)), "YES")

    def test_unordered_intervals(self):
        self.assertEqual(intersection((5, 1), (3, 7)), "NO")

    # --- Invalid Input Tests (Optional) ---
    def test_none_input(self):
        with self.assertRaises(TypeError):
            intersection(None, (1, 2))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            intersection("1,2", (1, 2))

    def test_single_value_tuple(self):
        with self.assertRaises(ValueError):
            intersection((1,), (2, 3))

    def test_three_element_tuple(self):
        with self.assertRaises(ValueError):
            intersection((1, 2, 3), (2, 3))

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            intersection(("a", "b"), (1, 2))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            intersection((1, "2"), (2, 3))

if __name__ == "__main__":
    unittest.main()
