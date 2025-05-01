import unittest
from code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    
    def test_example_1(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
    
    def test_example_2(self):
        self.assertEqual(decimal_to_binary(32), "db100000db")
    
    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")
    
    def test_one(self):
        self.assertEqual(decimal_to_binary(1), "db1db")
    
    def test_large_number(self):
        self.assertEqual(decimal_to_binary(1024), "db10000000000db")
    
    def test_power_of_two(self):
        self.assertEqual(decimal_to_binary(8), "db1000db")
    
    def test_random_number(self):
        self.assertEqual(decimal_to_binary(123), "db1111011db")

if __name__ == '__main__':
    unittest.main()