# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def reverse_delete(s, c):
    if not isinstance(s, str) or not isinstance(c, str):
        raise TypeError("Both inputs must be strings.")

    to_delete = set(c)
    result = ''.join(ch for ch in s if ch not in to_delete)

    is_palindrome = result == result[::-1]
    return result, is_palindrome
