# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import eat

class TestEatFunction(unittest.TestCase):
    
    # Standard Functional Tests
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
    
    # Edge Cases
    def test_zero_remaining(self):
        self.assertEqual(eat(10, 5, 0), [10, 0])

    def test_zero_need(self):
        self.assertEqual(eat(7, 0, 3), [7, 3])

    def test_zero_number(self):
        self.assertEqual(eat(0, 6, 10), [6, 4])

    def test_all_zeros(self):
        self.assertEqual(eat(0, 0, 0), [0, 0])
    
    def test_large_numbers(self):
        self.assertEqual(eat(1_000_000, 1_000_000, 1_000_000), [2_000_000, 0])

    def test_need_greater_than_remaining_by_one(self):
        self.assertEqual(eat(3, 6, 5), [8, 0])

    def test_remaining_exactly_equals_need(self):
        self.assertEqual(eat(2, 5, 5), [7, 0])

    def test_need_zero_remaining_zero(self):
        self.assertEqual(eat(3, 0, 0), [3, 0])

    def test_number_only_growth(self):
        self.assertEqual(eat(1, 0, 100), [1, 100])
    
    # Combinatorial Zeros
    def test_zero_need_and_remaining(self):
        self.assertEqual(eat(5, 0, 0), [5, 0])
        
    def test_zero_number_and_need(self):
        self.assertEqual(eat(0, 0, 7), [0, 7])
        
    def test_zero_number_and_remaining(self):
        self.assertEqual(eat(0, 5, 0), [0, 0])
    
    # Invalid Type Inputs
    def test_string_input(self):
        with self.assertRaises(TypeError):
            eat("5", 5, 5)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            eat(None, 3, 2)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            eat(5.5, 2, 1)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            eat([1], 2, 3)

    def test_dict_input(self):
        with self.assertRaises(TypeError):
            eat({"number": 1}, 2, 3)
    
    # Negative Inputs
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            eat(-1, 3, 4)

    def test_negative_need(self):
        with self.assertRaises(ValueError):
            eat(5, -2, 3)

    def test_negative_remaining(self):
        with self.assertRaises(ValueError):
            eat(5, 2, -3)

    # Extremely Large Numbers
    def test_extremely_large_values(self):
        big = 10**18
        self.assertEqual(eat(big, big, big), [big * 2, 0])

    def test_extremely_large_need_smaller_remaining(self):
        big = 10**18
        self.assertEqual(eat(big, big - 1, big), [big + (big - 1), 1])
    
    # Boolean Inputs (Python treats bool as int subclass)
    def test_boolean_inputs(self):
        self.assertEqual(eat(True, False, True), [1, 1])  # eat(1, 0, 1)
        self.assertEqual(eat(False, True, False), [0, 0])  # eat(0, 1, 0)
    
    # Mixing int and float (should error)
    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            eat(3, 2.0, 1)

    def test_string_numeric(self):
        with self.assertRaises(TypeError):
            eat("3", "2", "1")
    
    def test_partial_invalid(self):
        with self.assertRaises(TypeError):
            eat(1, "2", 3)

    # Unusual but valid inputs
    def test_zero_need_large_remaining(self):
        self.assertEqual(eat(10, 0, 1000000), [10, 1000000])

    def test_small_number_large_need_and_remaining(self):
        self.assertEqual(eat(1, 9999, 8888), [1 + 8888, 0])

    def test_equal_values(self):
        self.assertEqual(eat(5, 5, 5), [10, 0])
    
if __name__ == "__main__":
    unittest.main()
