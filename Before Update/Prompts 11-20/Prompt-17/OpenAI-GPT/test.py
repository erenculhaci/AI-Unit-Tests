# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import bf

class TestBF(unittest.TestCase):
    def test_case_1(self):
        # Example 1: Planets with multiple in-between
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_case_2(self):
        # Example 2: Planets with one in-between
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))

    def test_case_3(self):
        # Example 3: Planets with several in-between
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_case_4(self):
        # Invalid planet names
        self.assertEqual(bf("Pluto", "Earth"), ())
        self.assertEqual(bf("Mars", "Pluto"), ())

    def test_case_5(self):
        # Adjacent planets (no in-between)
        self.assertEqual(bf("Venus", "Earth"), ())

if __name__ == "__main__":
    unittest.main()