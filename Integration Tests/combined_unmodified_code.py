# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

from typing import List, Tuple

class RabbitCarrotAnalyzer:
    def __init__(self, initial_eaten: int, needed: int, carrot_stock: List[int]):
        self.initial_eaten = initial_eaten
        self.needed = needed
        self.carrot_stock = carrot_stock

    def analyze(self) -> Tuple[int, int, int, int]:
        """
        Executes a pipeline:
        1. Plucks the smallest even value from carrot_stock.
        2. Uses that as remaining carrots for 'eat'.
        3. Calls 'eat' and gets total_eaten.
        4. From 1 to total_eaten, counts even and odd palindromes.

        Returns:
            (plucked_value, total_eaten, even_palindromes, odd_palindromes)
            or (None, None, None, None) if no even pluckable value exists.
        """
        plucked = self._pluck(self.carrot_stock)
        if not plucked:
            return (None, None, None, None)
        
        remaining = plucked[0]
        total_eaten, _ = self._eat(self.initial_eaten, self.needed, remaining)
        even_p, odd_p = self._even_odd_palindrome(total_eaten)
        return (remaining, total_eaten, even_p, odd_p)

    @staticmethod
    def _pluck(arr: List[int]) -> List[int]:
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
        if remaining >= need:
            return [number + need, remaining - need]
        else:
            return [number + remaining, 0]

    @staticmethod
    def _even_odd_palindrome(n: int) -> Tuple[int, int]:
        even_count = 0
        odd_count = 0
        for i in range(1, n + 1):
            if str(i) == str(i)[::-1]:
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
        return (even_count, odd_count)
