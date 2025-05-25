import unittest
from code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(even_odd_palindrome(0), (0, 0))

    def test_lower_bound(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    def test_two(self):
        self.assertEqual(even_odd_palindrome(2), (1, 1))

    def test_upper_bound(self):
        even, odd = even_odd_palindrome(1000)
        self.assertEqual(even + odd, 108)  

    def test_example_1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_example_2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_medium_number(self):
        self.assertEqual(even_odd_palindrome(50), (6, 7)) 

    def test_double_digit_limit(self):
        self.assertEqual(even_odd_palindrome(99), (8, 10)) 

    def test_palindromes_up_to_101(self):
        self.assertEqual(even_odd_palindrome(101), (8, 11))  

    def test_non_palindromic_range(self):
        self.assertEqual(even_odd_palindrome(10), (4, 5))  

    def test_large_input(self):
        self.assertEqual(even_odd_palindrome(1000), (48, 60)) 

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            even_odd_palindrome(-5)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            even_odd_palindrome(10.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            even_odd_palindrome("100")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            even_odd_palindrome(None)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            even_odd_palindrome([1, 2, 3])

    def test_boolean_input(self):
        with self.assertRaises(TypeError):
            even_odd_palindrome(True)

    def test_dictionary_input(self):
        with self.assertRaises(TypeError):
            even_odd_palindrome({"n": 10})

if __name__ == '__main__':
    unittest.main()
