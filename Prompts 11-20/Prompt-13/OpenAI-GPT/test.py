# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import will_it_fly

class TestWillItFly(unittest.TestCase):
    def test_unbalanced_but_within_weight(self):
        # Test case where the list is unbalanced but within weight
        self.assertFalse(will_it_fly([1, 2], 5))

    def test_balanced_but_exceeds_weight(self):
        # Test case where the list is balanced but exceeds weight
        self.assertFalse(will_it_fly([3, 2, 3], 1))

    def test_balanced_and_within_weight(self):
        # Test case where the list is balanced and within weight
        self.assertTrue(will_it_fly([3, 2, 3], 9))

    def test_single_element_balanced_and_within_weight(self):
        # Test case with a single element that is balanced and within weight
        self.assertTrue(will_it_fly([3], 5))

if __name__ == "__main__":
    unittest.main()