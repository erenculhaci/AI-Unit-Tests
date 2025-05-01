# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import closest_integer

class TestClosestInteger(unittest.TestCase):
    def test_exact_integer(self):
        # Test with a value that is already an integer
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_decimal(self):
        # Test with a positive decimal value
        self.assertEqual(closest_integer("15.3"), 15)

    def test_round_away_from_zero_positive(self):
        # Test rounding away from zero for a positive equidistant value
        self.assertEqual(closest_integer("14.5"), 15)

    def test_round_away_from_zero_negative(self):
        # Test rounding away from zero for a negative equidistant value
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_negative_decimal(self):
        # Test with a negative decimal value
        self.assertEqual(closest_integer("-15.3"), -15)

if __name__ == "__main__":
    unittest.main()