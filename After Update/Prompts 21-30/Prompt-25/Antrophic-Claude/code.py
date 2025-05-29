def is_palindrome(s):
    """
    Determines whether a string is a palindrome.

    A palindrome is a sequence of characters that reads the same forward
    and backward, including all characters exactly as they appear,
    with no normalization.

    Args:
        s: A string to check

    Returns:
        bool: True if the input string is a palindrome, False otherwise

    Raises:
        TypeError: If the input is not a string
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Compare the string with its reverse
    # Case-sensitive comparison with all characters preserved
    return s == s[::-1]