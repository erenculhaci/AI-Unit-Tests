# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
import unittest
from code import closest_integer

class TestClosestInteger(unittest.TestCase):
    
    def test_whole_number(self):
        """Test with whole numbers as strings."""
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("-7"), -7)
    
    def test_decimal_less_than_half(self):
        """Test with decimal parts less than 0.5."""
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("-8.2"), -8)
    
    def test_decimal_greater_than_half(self):
        """Test with decimal parts greater than 0.5."""
        self.assertEqual(closest_integer("7.8"), 8)
        self.assertEqual(closest_integer("-3.7"), -4)
    
    def test_rounding_away_from_zero(self):
        """Test the special case of rounding away from zero when exactly at 0.5."""
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
    
    def test_edge_cases(self):
        """Test with edge cases like zero and very small numbers."""
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("0.5"), 1)  # Away from zero
        self.assertEqual(closest_integer("-0.5"), -1)  # Away from zero
        self.assertEqual(closest_integer("0.49"), 0)
        self.assertEqual(closest_integer("-0.49"), 0)

if __name__ == "__main__":
    unittest.main()