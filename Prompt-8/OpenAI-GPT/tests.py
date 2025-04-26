import unittest
from code import eat

class TestEatFunction(unittest.TestCase):
    
    def test_enough_carrots(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_barely_enough(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_more_need_than_remaining(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_exactly_needed(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test_no_need(self):
        self.assertEqual(eat(5, 0, 3), [5, 3])

if __name__ == "__main__":
    unittest.main()
