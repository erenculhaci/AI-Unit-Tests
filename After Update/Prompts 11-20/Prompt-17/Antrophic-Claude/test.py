import unittest
from code import bf

class TestBetweenPlanets(unittest.TestCase):
    
    def test_example_1(self):
        """Test the first example: planets between Jupiter and Neptune."""
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
    
    def test_example_2(self):
        """Test the second example: planets between Earth and Mercury."""
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))
    
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
        
    def test_adjacent_planets(self):
        """Test when planets are adjacent to each other."""
        self.assertEqual(bf("Mercury", "Venus"), ())
        self.assertEqual(bf("Venus", "Mercury"), ())
        self.assertEqual(bf("Earth", "Mars"), ())
        
    def test_case_sensitivity(self):
        """Test case sensitivity of planet names."""
        self.assertEqual(bf("jupiter", "Neptune"), ())
        self.assertEqual(bf("EARTH", "mars"), ())
        
    def test_reversed_order(self):
        """Test with planets in opposite order but same result."""
        self.assertEqual(bf("Neptune", "Jupiter"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Uranus", "Mercury"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
        
    def test_all_planets_between_extremes(self):
        """Test with the two extreme planets."""
        self.assertEqual(bf("Mercury", "Neptune"), 
                         ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))
        self.assertEqual(bf("Neptune", "Mercury"), 
                         ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))
        
    def test_one_invalid_one_valid(self):
        """Test with one valid and one invalid planet name."""
        self.assertEqual(bf("Mars", "Pluto"), ())
        self.assertEqual(bf("Ceres", "Saturn"), ())
        
    def test_empty_strings(self):
        """Test with empty strings."""
        self.assertEqual(bf("", "Mars"), ())
        self.assertEqual(bf("Earth", ""), ())
        self.assertEqual(bf("", ""), ())
        
    def test_non_string_inputs(self):
        """Test with non-string inputs."""
        self.assertEqual(bf(123, "Mars"), ())
        self.assertEqual(bf("Earth", None), ())
        self.assertEqual(bf(True, False), ())

if __name__ == "__main__":
    unittest.main()