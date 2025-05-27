# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def even_odd_palindrome(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer (not boolean).")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)

