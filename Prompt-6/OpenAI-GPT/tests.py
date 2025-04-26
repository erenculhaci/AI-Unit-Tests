import unittest
from code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):
    def test_example(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_starting_with_even(self):
        self.assertEqual(get_odd_collatz(6), [1, 3, 5])

    def test_one(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_large_number(self):
        result = get_odd_collatz(19)
        expected = [1, 5, 7, 11, 17, 19, 21, 31, 41, 47, 55, 61, 79]
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_odd_collatz(0)

if __name__ == '__main__':
    unittest.main()
