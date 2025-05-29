# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import intersection


class TestIntersection(unittest.TestCase):

    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_example_2(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_example_3(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_no_intersection(self):
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")
        self.assertEqual(intersection((5, 10), (11, 15)), "NO")

    def test_touching_intervals(self):
        self.assertEqual(intersection((1, 3), (3, 5)), "NO")
        self.assertEqual(intersection((0, 2), (2, 4)), "NO")

    def test_prime_length_2(self):
        self.assertEqual(intersection((1, 5), (2, 4)), "YES")
        self.assertEqual(intersection((0, 3), (1, 5)), "YES")

    def test_prime_length_3(self):
        self.assertEqual(intersection((0, 5), (2, 7)), "YES")
        self.assertEqual(intersection((1, 6), (3, 8)), "YES")

    def test_prime_length_5(self):
        self.assertEqual(intersection((0, 10), (3, 8)), "YES")
        self.assertEqual(intersection((-2, 5), (0, 7)), "YES")

    def test_prime_length_7(self):
        self.assertEqual(intersection((0, 10), (2, 9)), "YES")
        self.assertEqual(intersection((1, 12), (3, 10)), "YES")

    def test_non_prime_length_1(self):
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")
        self.assertEqual(intersection((0, 2), (1, 5)), "NO")

    def test_non_prime_length_4(self):
        self.assertEqual(intersection((1, 8), (3, 7)), "NO")
        self.assertEqual(intersection((0, 6), (2, 8)), "NO")

    def test_non_prime_length_6(self):
        self.assertEqual(intersection((1, 10), (3, 9)), "NO")
        self.assertEqual(intersection((0, 8), (2, 10)), "NO")

    def test_identical_intervals(self):
        self.assertEqual(intersection((1, 3), (1, 3)), "YES")
        self.assertEqual(intersection((0, 5), (0, 5)), "YES")
        self.assertEqual(intersection((2, 6), (2, 6)), "NO")

    def test_nested_intervals(self):
        self.assertEqual(intersection((1, 10), (3, 5)), "YES")
        self.assertEqual(intersection((0, 8), (2, 5)), "YES")
        self.assertEqual(intersection((1, 12), (4, 8)), "NO")

    def test_negative_intervals(self):
        self.assertEqual(intersection((-10, -5), (-8, -3)), "YES")
        self.assertEqual(intersection((-15, -10), (-12, -8)), "YES")
        self.assertEqual(intersection((-20, -15), (-18, -12)), "YES")

    def test_mixed_positive_negative(self):
        self.assertEqual(intersection((-5, 3), (-2, 1)), "YES")
        self.assertEqual(intersection((-3, 5), (0, 2)), "YES")
        self.assertEqual(intersection((-10, 0), (-5, 5)), "YES")

    def test_large_intervals(self):
        self.assertEqual(intersection((100, 200), (150, 180)), "NO")
        self.assertEqual(intersection((1000, 2000), (1500, 1502)), "YES")
        self.assertEqual(intersection((50, 100), (75, 78)), "YES")

    def test_zero_length_boundary(self):
        self.assertEqual(intersection((0, 0), (0, 0)), "NO")
        self.assertEqual(intersection((1, 1), (1, 1)), "NO")
        self.assertEqual(intersection((-1, -1), (-1, -1)), "NO")

    def test_order_independence(self):
        self.assertEqual(intersection((1, 5), (3, 7)), intersection((3, 7), (1, 5)))
        self.assertEqual(intersection((-2, 2), (0, 4)), intersection((0, 4), (-2, 2)))

    # --- Invalid Input Tests ---
    def test_non_tuple_input_integer(self):
        with self.assertRaises(TypeError):
            intersection(123, (1, 2))

    def test_non_tuple_input_string(self):
        with self.assertRaises(TypeError):
            intersection("invalid", (1, 2))

    def test_non_tuple_input_list(self):
        with self.assertRaises(TypeError):
            intersection([1, 2], (1, 2))

    def test_non_tuple_input_none(self):
        with self.assertRaises(TypeError):
            intersection(None, (1, 2))

    def test_wrong_tuple_size(self):
        with self.assertRaises(ValueError):
            intersection((1,), (1, 2))
        with self.assertRaises(ValueError):
            intersection((1, 2, 3), (1, 2))

    def test_non_numeric_tuple_elements(self):
        with self.assertRaises(TypeError):
            intersection(("a", "b"), (1, 2))
        with self.assertRaises(TypeError):
            intersection((1, 2), (None, 5))

    # --- Edge Cases for Prime Detection ---
    def test_large_prime_lengths(self):
        self.assertEqual(intersection((0, 100), (10, 41)), "YES")
        self.assertEqual(intersection((0, 150), (15, 52)), "YES")
        self.assertEqual(intersection((0, 200), (20, 63)), "YES")

    def test_large_composite_lengths(self):
        self.assertEqual(intersection((0, 20), (5, 19)), "NO")
        self.assertEqual(intersection((0, 25), (7, 23)), "NO")
        self.assertEqual(intersection((0, 30), (10, 28)), "NO")


if __name__ == "__main__":
    unittest.main()