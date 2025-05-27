# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from combined_modified_code import RabbitCarrotAnalyzer #change this file if you want to test combined_unmodified_code.py

class TestRabbitCarrotAnalyzerIntegration(unittest.TestCase):
    """Integration tests for RabbitCarrotAnalyzer class."""

    def test_basic_pipeline_flow(self):
        """Test basic pipeline: pluck -> eat -> palindrome count."""
        # Pluck 2 (smallest even), eat(3, 4, 2) -> total_eaten = 5
        # Palindromes 1-5: [1,2,3,4,5] -> even: 2,4 (count=2), odd: 1,3,5 (count=3)
        analyzer = RabbitCarrotAnalyzer(3, 4, [5, 2, 7, 8])
        result = analyzer.analyze()
        self.assertEqual(result, (2, 5, 2, 3))

    def test_no_even_numbers_available(self):
        """Test when no even numbers exist in carrot stock."""
        analyzer = RabbitCarrotAnalyzer(10, 5, [1, 3, 5, 7, 9])
        result = analyzer.analyze()
        self.assertEqual(result, (None, None, None, None))

    def test_empty_carrot_stock(self):
        """Test with empty carrot stock."""
        analyzer = RabbitCarrotAnalyzer(5, 3, [])
        result = analyzer.analyze()
        self.assertEqual(result, (None, None, None, None))

    def test_zero_as_smallest_even(self):
        """Test when 0 is the smallest even number."""
        # Pluck 0, eat(2, 3, 0) -> total_eaten = 2
        # Palindromes 1-2: [1,2] -> even: 2 (count=1), odd: 1 (count=1)
        analyzer = RabbitCarrotAnalyzer(2, 3, [1, 0, 4, 6])
        result = analyzer.analyze()
        self.assertEqual(result, (0, 2, 1, 1))

    def test_exact_need_fulfillment(self):
        """Test when remaining carrots exactly match the need."""
        # Pluck 4, eat(6, 4, 4) -> total_eaten = 10
        # Palindromes 1-10: [1,2,3,4,5,6,7,8,9] -> even: 2,4,6,8 (count=4), odd: 1,3,5,7,9 (count=5)
        analyzer = RabbitCarrotAnalyzer(6, 4, [8, 4, 10, 12])
        result = analyzer.analyze()
        self.assertEqual(result, (4, 10, 4, 5))

    def test_insufficient_carrots(self):
        """Test when remaining carrots are less than needed."""
        # Pluck 2, eat(5, 10, 2) -> total_eaten = 7
        # Palindromes 1-7: [1,2,3,4,5,6,7] -> even: 2,4,6 (count=3), odd: 1,3,5,7 (count=4)
        analyzer = RabbitCarrotAnalyzer(5, 10, [3, 2, 7])
        result = analyzer.analyze()
        self.assertEqual(result, (2, 7, 3, 4))

    def test_multiple_same_smallest_even(self):
        """Test when there are multiple instances of the smallest even number."""
        # Should pick the first occurrence: pluck 4 at index 0
        # eat(1, 5, 4) -> total_eaten = 5
        # Palindromes 1-5: [1,2,3,4,5] -> even: 2,4 (count=2), odd: 1,3,5 (count=3)
        analyzer = RabbitCarrotAnalyzer(1, 5, [4, 6, 4, 8])
        result = analyzer.analyze()
        self.assertEqual(result, (4, 5, 2, 3))

    def test_negative_even_numbers(self):
        """Test with negative even numbers (should pick the smallest)."""
        # Pluck -6 (smallest even), eat(10, 3, -6) -> would be invalid in real scenario
        # But following the logic: eat(10, 3, -6) -> total_eaten = 4 (10 + (-6))
        # This test shows edge case behavior
        analyzer = RabbitCarrotAnalyzer(10, 3, [-4, -6, 1, 3])
        result = analyzer.analyze()
        self.assertEqual(result, (-6, 4, 2, 2))  # Palindromes 1-4: even=2,4 (2), odd=1,3 (2)

    def test_large_numbers_integration(self):
        """Test with larger numbers to verify scalability."""
        # Pluck 100, eat(50, 75, 100) -> total_eaten = 125
        analyzer = RabbitCarrotAnalyzer(50, 75, [101, 100, 999])
        result = analyzer.analyze()
        expected_even, expected_odd = analyzer._even_odd_palindrome(125)
        self.assertEqual(result, (100, 125, expected_even, expected_odd))

    def test_zero_initial_eaten(self):
        """Test with zero initial eaten carrots."""
        # Pluck 6, eat(0, 8, 6) -> total_eaten = 6
        # Palindromes 1-6: [1,2,3,4,5,6] -> even: 2,4,6 (count=3), odd: 1,3,5 (count=3)
        analyzer = RabbitCarrotAnalyzer(0, 8, [7, 6, 9])
        result = analyzer.analyze()
        self.assertEqual(result, (6, 6, 3, 3))

    def test_zero_needed(self):
        """Test with zero needed carrots."""
        # Pluck 8, eat(15, 0, 8) -> total_eaten = 15
        analyzer = RabbitCarrotAnalyzer(15, 0, [9, 8, 11])
        result = analyzer.analyze()
        expected_even, expected_odd = analyzer._even_odd_palindrome(15)
        self.assertEqual(result, (8, 15, expected_even, expected_odd))

    def test_single_even_carrot(self):
        """Test with only one even carrot in stock."""
        # Pluck 12, eat(3, 7, 12) -> total_eaten = 10
        # Palindromes 1-10: [1,2,3,4,5,6,7,8,9] -> even: 2,4,6,8 (count=4), odd: 1,3,5,7,9 (count=5)
        analyzer = RabbitCarrotAnalyzer(3, 7, [1, 3, 12, 5])
        result = analyzer.analyze()
        self.assertEqual(result, (12, 10, 4, 5))

    def test_all_even_numbers(self):
        """Test when all numbers in stock are even."""
        # Should pick the smallest: 2
        # eat(4, 6, 2) -> total_eaten = 6
        # Palindromes 1-6: [1,2,3,4,5,6] -> even: 2,4,6 (count=3), odd: 1,3,5 (count=3)
        analyzer = RabbitCarrotAnalyzer(4, 6, [8, 2, 4, 10])
        result = analyzer.analyze()
        self.assertEqual(result, (2, 6, 3, 3))

    def test_palindrome_edge_cases(self):
        """Test edge cases for palindrome counting."""
        # Test when total_eaten results in interesting palindrome counts
        # Pluck 10, eat(1, 10, 10) -> total_eaten = 11
        # Palindromes 1-11: [1,2,3,4,5,6,7,8,9,11] -> even: 2,4,6,8 (count=4), odd: 1,3,5,7,9,11 (count=6)
        analyzer = RabbitCarrotAnalyzer(1, 10, [11, 10, 13])
        result = analyzer.analyze()
        self.assertEqual(result, (10, 11, 4, 6))

    def test_high_total_eaten_palindromes(self):
        """Test with higher total_eaten to verify palindrome counting."""
        # Pluck 200, eat(99, 100, 200) -> total_eaten = 199
        analyzer = RabbitCarrotAnalyzer(99, 100, [201, 200, 203])
        result = analyzer.analyze()
        # Manually verify palindromes up to 199
        expected_even, expected_odd = analyzer._even_odd_palindrome(199)
        self.assertEqual(result, (200, 199, expected_even, expected_odd))

    def test_consistency_across_multiple_calls(self):
        """Test that multiple calls to analyze() return consistent results."""
        analyzer = RabbitCarrotAnalyzer(5, 3, [2, 4, 6, 1])
        result1 = analyzer.analyze()
        result2 = analyzer.analyze()
        result3 = analyzer.analyze()
        self.assertEqual(result1, result2)
        self.assertEqual(result2, result3)

    def test_different_instances_same_parameters(self):
        """Test that different instances with same parameters give same results."""
        params = (7, 5, [3, 8, 2, 9])
        analyzer1 = RabbitCarrotAnalyzer(*params)
        analyzer2 = RabbitCarrotAnalyzer(*params)
        result1 = analyzer1.analyze()
        result2 = analyzer2.analyze()
        self.assertEqual(result1, result2)

    def test_complex_scenario_verification(self):
        """Test a complex scenario with manual verification."""
        # Complex case: mixed positive/negative, multiple evens
        # Stock: [-2, 5, 0, 8, -4, 3]
        # Smallest even: -4 at index 4
        # eat(12, 8, -4) -> total_eaten = 8 (12 + (-4), since -4 < 8)
        # Palindromes 1-8: [1,2,3,4,5,6,7,8] -> even: 2,4,6,8 (count=4), odd: 1,3,5,7 (count=4)
        analyzer = RabbitCarrotAnalyzer(12, 8, [-2, 5, 0, 8, -4, 3])
        result = analyzer.analyze()
        self.assertEqual(result, (-4, 8, 4, 4))

if __name__ == '__main__':
    unittest.main()