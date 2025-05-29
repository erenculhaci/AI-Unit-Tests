# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea:
    - Find the longest suffix of the string that is a palindrome.
    - Append the reverse of the prefix before the palindromic suffix to the string.
    """
    if not string:
        return ""

    # Helper function to check if a string is a palindrome
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    # Iterate through the string to find the longest palindromic suffix
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            prefix = string[:i]
            return string + prefix[::-1]

    # If no palindromic suffix is found (should not happen), return the string
    return string + string[::-1][1:]