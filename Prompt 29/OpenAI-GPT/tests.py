import unittest
from code import intersection

class TestIntersection(unittest.TestCase):

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

if __name__ == "__main__":
    unittest.main()
