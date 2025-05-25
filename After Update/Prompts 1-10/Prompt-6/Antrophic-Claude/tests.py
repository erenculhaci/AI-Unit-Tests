# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_basic_values(self):
        self.assertEqual(get_odd_collatz(1), [1])
        self.assertEqual(get_odd_collatz(2), [1])
        self.assertEqual(get_odd_collatz(3), [1, 3, 5])
        self.assertEqual(get_odd_collatz(5), [1, 5])
        self.assertEqual(get_odd_collatz(7), [1, 5, 7, 11, 13, 17])
        self.assertEqual(get_odd_collatz(10), [1, 5])

    def test_medium_sequences(self):
        self.assertEqual(get_odd_collatz(9), [1, 5, 7, 9, 11, 13, 17])
        self.assertEqual(get_odd_collatz(13), [1, 5, 13])
        self.assertEqual(get_odd_collatz(17), [1, 5, 13, 17])
        self.assertEqual(get_odd_collatz(19), [1, 5, 11, 13, 17, 19, 29])
        self.assertEqual(get_odd_collatz(27), [
            1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121,
            137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377,
            395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619,
            2051, 2429, 3077
        ])

    def test_large_input(self):
        result = get_odd_collatz(97)
        self.assertIsInstance(result, list)
        self.assertIn(1, result)
        self.assertTrue(all(x % 2 == 1 for x in result))

    def test_larger_even(self):
        result = get_odd_collatz(100)
        self.assertIsInstance(result, list)
        self.assertIn(1, result)
        self.assertTrue(all(x % 2 == 1 for x in result))

    def test_edge_cases(self):
        self.assertEqual(get_odd_collatz(4), [1])
        self.assertEqual(get_odd_collatz(8), [1])
        self.assertEqual(get_odd_collatz(16), [1])
        self.assertEqual(get_odd_collatz(32), [1])

    def test_invalid_zero_negative(self):
        with self.assertRaises(ValueError):
            get_odd_collatz(0)
        with self.assertRaises(ValueError):
            get_odd_collatz(-1)
        with self.assertRaises(ValueError):
            get_odd_collatz(-999)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            get_odd_collatz(None)
        with self.assertRaises(TypeError):
            get_odd_collatz("10")
        with self.assertRaises(TypeError):
            get_odd_collatz("abc")
        with self.assertRaises(TypeError):
            get_odd_collatz([10])
        with self.assertRaises(TypeError):
            get_odd_collatz((5,))
        with self.assertRaises(TypeError):
            get_odd_collatz({1: 2})

        with self.assertRaises(ValueError):
            get_odd_collatz(False)
        self.assertEqual(get_odd_collatz(True), [1])

    def test_invalid_floats(self):
        with self.assertRaises(TypeError):
            get_odd_collatz(5.5)
        with self.assertRaises(TypeError):
            get_odd_collatz(10.0)


    def test_very_large_input(self):
        result = get_odd_collatz(999999)
        self.assertIsInstance(result, list)
        self.assertIn(1, result)
        self.assertTrue(all(x % 2 == 1 for x in result))

    def test_order_and_uniqueness(self):
        result = get_odd_collatz(27)
        self.assertEqual(result, sorted(set(result)))  # expect sorted list with no duplicates
        self.assertTrue(all(x % 2 == 1 for x in result))

if __name__ == '__main__':
    unittest.main()
