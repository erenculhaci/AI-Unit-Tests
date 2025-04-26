import unittest
from code import maximum

class TestMaximumFunction(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_example2(self):
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])

    def test_example3(self):
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_k_zero(self):
        self.assertEqual(maximum([1, 2, 3], 0), [])

    def test_duplicates(self):
        self.assertEqual(maximum([5, 5, 5, 1], 2), [5, 5])

if __name__ == "__main__":
    unittest.main()
