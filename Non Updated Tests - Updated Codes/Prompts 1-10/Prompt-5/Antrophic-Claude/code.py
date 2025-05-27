# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def even_odd_palindrome(n):
    # Input validation
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Handle edge case
    if n == 0:
        return (0, 0)
    
    def is_palindrome(num):
        """Check if a number is a palindrome"""
        str_num = str(num)
        return str_num == str_num[::-1]
    
    even_count = 0
    odd_count = 0
    
    # Count palindromes from 1 to n (inclusive)
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)