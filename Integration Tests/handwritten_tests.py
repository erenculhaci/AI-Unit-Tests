# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from combined_modified_code import RabbitCarrotAnalyzer #change this file if you want to test combined_unmodified_code.py

class TestRabbitCarrotAnalyzer(unittest.TestCase):
    
    # ========== INITIALIZATION TESTS ==========
    
    def test_valid_initialization(self):
        """Test valid initialization cases."""
        analyzer = RabbitCarrotAnalyzer(5, 3, [1, 2, 3, 4])
        self.assertEqual(analyzer.initial_eaten, 5)
        self.assertEqual(analyzer.needed, 3)
        self.assertEqual(analyzer.carrot_stock, [1, 2, 3, 4])

    def test_zero_values_initialization(self):
        """Test initialization with zero values."""
        analyzer = RabbitCarrotAnalyzer(0, 0, [0, 2, 4])
        self.assertEqual(analyzer.initial_eaten, 0)
        self.assertEqual(analyzer.needed, 0)

    def test_empty_stock_initialization(self):
        """Test initialization with empty carrot stock."""
        analyzer = RabbitCarrotAnalyzer(5, 3, [])
        self.assertEqual(analyzer.carrot_stock, [])

    # ========== INITIALIZATION ERROR TESTS ==========
    
    def test_invalid_initial_eaten_type(self):
        """Test invalid types for initial_eaten."""
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer("5", 3, [1, 2])
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5.5, 3, [1, 2])
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(None, 3, [1, 2])
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(True, 3, [1, 2])  # Boolean not allowed

    def test_invalid_needed_type(self):
        """Test invalid types for needed."""
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, "3", [1, 2])
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, [3], [1, 2])

    def test_invalid_carrot_stock_type(self):
        """Test invalid types for carrot_stock."""
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, 3, "123")
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, 3, {1, 2, 3})
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, 3, None)

    def test_invalid_carrot_stock_elements(self):
        """Test invalid elements in carrot_stock."""
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, 3, [1, "2", 3])
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, 3, [1, 2.5, 3])
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, 3, [1, None, 3])
        with self.assertRaises(TypeError):
            RabbitCarrotAnalyzer(5, 3, [1, True, 3])  # Boolean not allowed

    def test_negative_values(self):
        """Test negative input values."""
        with self.assertRaises(ValueError):
            RabbitCarrotAnalyzer(-1, 3, [1, 2])
        with self.assertRaises(ValueError):
            RabbitCarrotAnalyzer(5, -3, [1, 2])

    # ========== SUCCESSFUL ANALYSIS TESTS ==========
    
    def test_basic_analysis_flow(self):
        """Test basic successful analysis flow."""
        # Stock: [5, 2, 7, 8] -> pluck 2 (smallest even)
        # eat(3, 4, 2) -> since 2 < 4, eat all 2 -> total = 3 + 2 = 5
        # palindromes 1-5: 1,2,3,4,5 -> even: 2,4 (count=2), odd: 1,3,5 (count=3)
        analyzer = RabbitCarrotAnalyzer(3, 4, [5, 2, 7, 8])
        result = analyzer.analyze()
        self.assertEqual(result, (2, 5, 2, 3))

    def test_sufficient_carrots_analysis(self):
        """Test analysis when plucked carrots are sufficient."""
        # Stock: [10, 6, 8] -> pluck 6 (smallest even)
        # eat(2, 3, 6) -> since 6 >= 3, eat 3 -> total = 2 + 3 = 5
        analyzer = RabbitCarrotAnalyzer(2, 3, [10, 6, 8])
        result = analyzer.analyze()
        self.assertEqual(result, (6, 5, 2, 3))

    def test_zero_plucked_carrot(self):
        """Test analysis with zero as plucked carrot."""
        # Stock: [0, 3, 5] -> pluck 0
        # eat(5, 10, 0) -> eat all 0 -> total = 5 + 0 = 5
        analyzer = RabbitCarrotAnalyzer(5, 10, [0, 3, 5])
        result = analyzer.analyze()
        self.assertEqual(result, (0, 5, 2, 3))

    def test_large_numbers_analysis(self):
        """Test analysis with large numbers."""
        analyzer = RabbitCarrotAnalyzer(100, 50, [200, 150, 300])
        result = analyzer.analyze()
        # Pluck 150, eat(100, 50, 150) -> total = 150, palindromes need calculation
        expected_even, expected_odd = analyzer._even_odd_palindrome(150)
        self.assertEqual(result, (150, 150, expected_even, expected_odd))

    def test_multiple_same_smallest_even(self):
        """Test when multiple instances of smallest even exist."""
        # Should pick the first one occurring smallest even
        analyzer = RabbitCarrotAnalyzer(1, 1, [3, 2, 5, 2, 7])
        result = analyzer.analyze()
        # Pluck 2 (index 1), eat(1, 1, 2) -> total = 2
        self.assertEqual(result, (2, 2, 1, 1))

    def test_negative_carrots_in_stock(self):
        """Test analysis with negative carrots in stock."""
        # Stock: [-4, 3, -2, 5] -> pluck -4 (smallest even)
        analyzer = RabbitCarrotAnalyzer(10, 5, [-4, 3, -2, 5])
        result = analyzer.analyze()
        # eat(10, 5, -4) -> since -4 < 5, eat all -4... but negative eating?
        # This should actually be handled by eat function - eating negative carrots
        #  Eat function does: eat(10, 5, -4) -> total = 10 + (-4) = 6
        self.assertEqual(result, (-4, 6, 3, 3))  # palindromes 1-6: even=2,4,6, odd=1,3,5

    # ========== FAILED ANALYSIS TESTS ==========
    
    def test_no_even_carrots_analysis(self):
        """Test analysis when no even carrots exist."""
        analyzer = RabbitCarrotAnalyzer(5, 3, [1, 3, 5, 7])
        result = analyzer.analyze()
        self.assertEqual(result, (None, None, None, None))

    def test_empty_stock_analysis(self):
        """Test analysis with empty carrot stock."""
        analyzer = RabbitCarrotAnalyzer(5, 3, [])
        result = analyzer.analyze()
        self.assertEqual(result, (None, None, None, None))
        
    def insufficient_carrots_analysis(self):
        """Test analysis when remaining carrots are less than needed."""
        # Stock: [1, 2, 3] -> pluck 2 (smallest even)
        # eat(5, 10, 2) -> since 2 < 10, eat all 2 -> total = 5 + 2 = 7
        analyzer = RabbitCarrotAnalyzer(5, 10, [1, 2, 3])
        result = analyzer.analyze()
        self.assertEqual(result, (2, 7, 3, 4))

    # ========== EDGE CASES ==========
    
    def test_zero_needed_carrots(self):
        """Test when no additional carrots are needed."""
        # eat(5, 0, 4) -> total = 5 + 0 = 5
        analyzer = RabbitCarrotAnalyzer(5, 0, [4, 3, 6])
        result = analyzer.analyze()
        self.assertEqual(result, (4, 5, 2, 3))

    def test_zero_initial_eaten(self):
        """Test when no carrots were initially eaten."""
        analyzer = RabbitCarrotAnalyzer(0, 5, [6, 3, 8])
        result = analyzer.analyze()
        # Pluck 6, eat(0, 5, 6) -> total = 5
        self.assertEqual(result, (6, 5, 2, 3))

    def test_all_zeros(self):
        """Test analysis with all zero values."""
        analyzer = RabbitCarrotAnalyzer(0, 0, [0, 1, 3])
        result = analyzer.analyze()
        # Pluck 0, eat(0, 0, 0) -> total = 0, palindromes from 1 to 0 = (0,0)
        self.assertEqual(result, (0, 0, 0, 0))

    def test_single_carrot_stock(self):
        """Test with single carrot in stock."""
        analyzer = RabbitCarrotAnalyzer(3, 2, [4])
        result = analyzer.analyze()
        self.assertEqual(result, (4, 5, 2, 3))

    def test_all_even_carrots(self):
        """Test with all even carrots in stock."""
        analyzer = RabbitCarrotAnalyzer(1, 3, [8, 2, 6, 4])
        result = analyzer.analyze()
        # Should pluck 2 (smallest even)
        self.assertEqual(result, (2, 3, 1, 2))  # palindromes 1-3: even=2, odd=1,3
        
    def test_single_even_carrot(self):
        """Test with a single even carrot in stock."""
        analyzer = RabbitCarrotAnalyzer(2, 1, [6])
        result = analyzer.analyze()
        # Pluck 6, eat(2, 1, 6) -> total = 3
        self.assertEqual(result, (6, 3, 1, 2))
    
    def test_complex_negative_stock_palindrome_edge_case(self):
        """Test complex scenario with negative stock and higher palindrome range."""
        analyzer = RabbitCarrotAnalyzer(5, 10, [-10, -20, -3, -4, -15, -2])
        result = analyzer.analyze()
        self.assertEqual(result, (-20, -15, 0, 0))


    # ========== PALINDROME EDGE CASES ==========
    
    def test_high_palindrome_count(self):
        """Test analysis resulting in high palindrome counts."""
        analyzer = RabbitCarrotAnalyzer(50, 50, [100])
        result = analyzer.analyze()
        # Total eaten = 100, need to count palindromes 1-100
        expected_even, expected_odd = analyzer._even_odd_palindrome(100)
        self.assertEqual(result, (100, 100, expected_even, expected_odd))

    def test_palindrome_boundary_cases(self):
        """Test palindrome counting at various boundaries."""
        # Test at palindrome boundaries like 9->10, 99->100, etc.
        test_cases = [
            (4, 1, [10], 5)  ,  # Pluck 10, eat(4, 1, 10) -> total = 5
            (90, 9, [100], 99), # Just before 100
            (1, 10, [12], 11),  # Include 11 (first double-digit palindrome)
        ]
        
        for initial, needed, stock, expected_total in test_cases:
            with self.subTest(total=expected_total):
                analyzer = RabbitCarrotAnalyzer(initial, needed, stock)
                result = analyzer.analyze()
                expected_even, expected_odd = analyzer._even_odd_palindrome(expected_total)
                self.assertEqual(result, (stock[0], expected_total, expected_even, expected_odd))

    # ========== SUMMARY FUNCTIONALITY TESTS ==========
    
    def test_analysis_summary_success(self):
        """Test summary generation for successful analysis."""
        analyzer = RabbitCarrotAnalyzer(3, 4, [5, 2, 7, 8])
        summary = analyzer.get_analysis_summary()
        self.assertIn("Plucked carrot value: 2", summary)
        self.assertIn("Total carrots eaten: 5", summary)
        self.assertIn("Even palindromes", summary)
        self.assertIn("Odd palindromes", summary)

    def test_analysis_summary_failure(self):
        """Test summary generation for failed analysis."""
        analyzer = RabbitCarrotAnalyzer(5, 3, [1, 3, 5])
        summary = analyzer.get_analysis_summary()
        self.assertIn("Analysis failed", summary)
        self.assertIn("No even carrots", summary)

    # ========== STRESS TESTS ==========
    
    def test_large_carrot_stock(self):
        """Test with very large carrot stock."""
        large_stock = list(range(1000, 0, -1))  # 1000 down to 1
        analyzer = RabbitCarrotAnalyzer(1, 1, large_stock)
        result = analyzer.analyze()
        # Should pluck 2 (smallest even), total = 2
        self.assertEqual(result, (2, 2, 1, 1))

    def test_performance_with_large_palindrome_range(self):
        """Test performance with large palindrome counting range."""
        analyzer = RabbitCarrotAnalyzer(500, 500, [1000])
        result = analyzer.analyze()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 1000)  # Plucked value
        self.assertEqual(result[1], 1000)  # Total eaten
        
if __name__ == "__main__":
    unittest.main(verbosity=2)