# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import bf

class TestBetweenPlanets(unittest.TestCase):
    
    def test_example_1(self):
        """Test the first example: planets between Jupiter and Neptune."""
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
    
    def test_example_2(self):
        """Test the second example: planets between Earth and Mercury."""
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))
    
    def test_example_3(self):
        """Test the third example: planets between Mercury and Uranus."""
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
    
    def test_invalid_planet(self):
        """Test with an invalid planet name."""
        self.assertEqual(bf("Pluto", "Mars"), ())
        self.assertEqual(bf("Earth", "Moon"), ())
    
    def test_same_planet(self):
        """Test when both input planets are the same."""
        self.assertEqual(bf("Mars", "Mars"), ())

if __name__ == "__main__":
    unittest.main()