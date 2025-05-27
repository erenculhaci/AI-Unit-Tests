# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

from typing import List, Tuple, Union, Optional

class RabbitCarrotAnalyzer:
    """
    A comprehensive class integrating three functions into a single analysis pipeline.
    """
    
    def __init__(self, initial_eaten: int, needed: int, carrot_stock: List[int]):
        """
        Initialize the analyzer with input validations.
        
        Args:
            initial_eaten: Number of carrots already eaten (non-negative integer)
            needed: Number of carrots needed to eat (non-negative integer)
            carrot_stock: List of available carrots (list of integers)
        
        Raises:
            TypeError: If inputs are not of correct types
            ValueError: If numerical inputs are negative
        """
        # Type validation
        if not isinstance(initial_eaten, int) or isinstance(initial_eaten, bool):
            raise TypeError("initial_eaten must be an integer")
        if not isinstance(needed, int) or isinstance(needed, bool):
            raise TypeError("needed must be an integer")
        if not isinstance(carrot_stock, list):
            raise TypeError("carrot_stock must be a list")
        
        # Value validation
        if initial_eaten < 0:
            raise ValueError("initial_eaten cannot be negative")
        if needed < 0:
            raise ValueError("needed cannot be negative")
        
        # Validate carrot_stock elements
        for i, carrot in enumerate(carrot_stock):
            if not isinstance(carrot, int) or isinstance(carrot, bool):
                raise TypeError(f"All carrot_stock elements must be integers, found {type(carrot).__name__} at index {i}")
        
        self.initial_eaten = initial_eaten
        self.needed = needed
        self.carrot_stock = carrot_stock

    def analyze(self) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[int]]:
        """
        Execute the complete analysis pipeline:
        1. Pluck the smallest even carrot from stock
        2. Use plucked carrot as remaining carrots for eating simulation
        3. Calculate total carrots eaten
        4. Count even and odd palindromes from 1 to total_eaten
        
        Returns:
            Tuple of (plucked_value, total_eaten, even_palindromes, odd_palindromes)
            Returns (None, None, None, None) if no even carrot can be plucked
        """
        try:
            # Step 1: Pluck smallest even carrot
            plucked_result = self._pluck(self.carrot_stock)
            if not plucked_result:
                return (None, None, None, None)
            
            plucked_value = plucked_result[0]
            
            # Step 2: Simulate eating with plucked carrot as remaining
            eating_result = self._eat(self.initial_eaten, self.needed, plucked_value)
            total_eaten = eating_result[0]
            
            # Step 3: Count palindromes
            even_palindromes, odd_palindromes = self._even_odd_palindrome(total_eaten)
            
            return (plucked_value, total_eaten, even_palindromes, odd_palindromes)
            
        except Exception as e:
            # Re-raise any unexpected errors with context
            raise RuntimeError(f"Analysis pipeline failed: {str(e)}") from e

    def get_analysis_summary(self) -> str:
        """
        Get a human-readable summary of the analysis.
        """
        result = self.analyze()
        if result[0] is None:
            return "Analysis failed: No even carrots available to pluck from stock"
        
        plucked, total_eaten, even_p, odd_p = result
        return (f"Analysis Summary:\n"
                f"- Plucked carrot value: {plucked}\n"
                f"- Total carrots eaten: {total_eaten}\n"
                f"- Even palindromes (1 to {total_eaten}): {even_p}\n"
                f"- Odd palindromes (1 to {total_eaten}): {odd_p}\n"
                f"- Total palindromes: {even_p + odd_p}")

    @staticmethod
    def _pluck(arr: List[int]) -> List[int]:
        """Find and return the smallest even value with its index."""
        if not arr:
            return []
        
        smallest_even = float('inf')
        smallest_index = -1
        
        for i, num in enumerate(arr):
            if num % 2 == 0 and num < smallest_even:
                smallest_even = num
                smallest_index = i
        
        return [] if smallest_index == -1 else [smallest_even, smallest_index]

    @staticmethod
    def _eat(number: int, need: int, remaining: int) -> List[int]:
        """Simulate eating carrots with given constraints."""
        if remaining >= need:
            return [number + need, remaining - need]
        else:
            return [number + remaining, 0]

    @staticmethod
    def _even_odd_palindrome(n: int) -> Tuple[int, int]:
        """Count even and odd palindromes from 1 to n (inclusive)."""
        if n <= 0:
            return (0, 0)
        
        even_count = 0
        odd_count = 0
        
        for i in range(1, n + 1):
            if str(i) == str(i)[::-1]:  # Check if palindrome
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
        
        return (even_count, odd_count)