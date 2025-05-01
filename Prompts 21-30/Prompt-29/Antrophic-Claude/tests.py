import unittest
from code import intersection

class TestIntersection(unittest.TestCase):
    
    def test_example_1(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
    
    def test_example_2(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
    
    def test_example_3(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")
    
    def test_no_intersection(self):
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")
    
    def test_prime_length_2(self):
        self.assertEqual(intersection((1, 5), (2, 4)), "YES")
    
    def test_prime_length_3(self):
        self.assertEqual(intersection((0, 5), (2, 7)), "YES")
    
    def test_zero_length(self):
        self.assertEqual(intersection((1, 2), (2, 5)), "NO")
    
    def test_large_intervals(self):
        self.assertEqual(intersection((10, 20), (15, 18)), "NO")

if __name__ == '__main__':
    unittest.main()