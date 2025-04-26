import unittest
from code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(get_odd_collatz(1), [1])
        self.assertEqual(get_odd_collatz(5), [1, 5])
        self.assertEqual(get_odd_collatz(10), [1, 5])
        
    def test_larger_numbers(self):
        # For n=27, the Collatz sequence is:
        # 27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 
        # 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 
        # 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 
        # 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 
        # 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 
        # 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 
        # 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
        self.assertEqual(get_odd_collatz(27), 
                         [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 
                          137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 
                          395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 
                          2051, 2429, 3077])
        
        # For n=17, the Collatz sequence is:
        # 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
        self.assertEqual(get_odd_collatz(17), [1, 5, 13, 17])
        
    def test_edge_cases(self):
        # Test with a large even number (16)
        # Sequence: 16, 8, 4, 2, 1
        self.assertEqual(get_odd_collatz(16), [1])
        
        # Test with 2
        # Sequence: 2, 1
        self.assertEqual(get_odd_collatz(2), [1])
        
    def test_error_handling(self):
        # Test that it raises ValueError for non-positive integers
        with self.assertRaises(ValueError):
            get_odd_collatz(0)
        
        with self.assertRaises(ValueError):
            get_odd_collatz(-5)

if __name__ == '__main__':
    unittest.main()