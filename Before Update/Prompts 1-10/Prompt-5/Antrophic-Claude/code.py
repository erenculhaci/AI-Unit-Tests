# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        # Convert the number to string to check if it's a palindrome
        str_i = str(i)
        if str_i == str_i[::-1]:  # Check if the string is a palindrome
            if i % 2 == 0:  # Check if the number is even
                even_count += 1
            else:  # The number is odd
                odd_count += 1
    
    return (even_count, odd_count)