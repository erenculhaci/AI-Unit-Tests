import unittest
from code import find_zero

class TestFindZero(unittest.TestCase):
    
    def test_linear_polynomial(self):
        """Test finding zeros of linear polynomials."""
        # f(x) = 1 + 2x, zero at x = -0.5
        result = find_zero([1, 2])
        self.assertAlmostEqual(result, -0.5, places=10)
        
        # f(x) = -3 + 6x, zero at x = 0.5
        result = find_zero([-3, 6])
        self.assertAlmostEqual(result, 0.5, places=10)
    
    def test_cubic_polynomial(self):
        """Test finding zeros of cubic polynomials."""
        # f(x) = -6 + 11x - 6x^2 + x^3 = (x-1)(x-2)(x-3)
        # Zeros at x = 1, 2, 3
        result = find_zero([-6, 11, -6, 1])
        # Should find one of the zeros
        self.assertTrue(abs(result - 1.0) < 1e-10 or 
                       abs(result - 2.0) < 1e-10 or 
                       abs(result - 3.0) < 1e-10)
    
    def test_higher_degree_polynomial(self):
        """Test finding zeros of higher degree polynomials."""
        # f(x) = x^4 - 5x^2 + 4 = (x^2 - 1)(x^2 - 4) = (x-1)(x+1)(x-2)(x+2)
        # Zeros at x = -2, -1, 1, 2
        result = find_zero([4, 0, -5, 0, 1])
        # Should find one of the zeros
        self.assertTrue(abs(result - 1.0) < 1e-10 or 
                       abs(result + 1.0) < 1e-10 or
                       abs(result - 2.0) < 1e-10 or 
                       abs(result + 2.0) < 1e-10)
    
    def test_even_coefficient_requirement(self):
        """Test that function raises error with odd number of coefficients."""
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])
    
    def test_nonzero_highest_coefficient(self):
        """Test that function raises error when highest coefficient is zero."""
        with self.assertRaises(ValueError):
            find_zero([1, 2, 0, 0])

if __name__ == '__main__':
    unittest.main()