# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s == s[::-1]
