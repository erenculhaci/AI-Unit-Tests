def reverse_delete(s, c):
    """
    Removes all characters from string s that are present in string c,
    and returns a tuple (new_string, is_palindrome).

    Args:
        s: The input string to process
        c: The string containing characters to delete from s

    Returns:
        tuple: (new_string, is_palindrome) where:
            - new_string is s with all characters in c removed
            - is_palindrome is True if new_string is a palindrome

    Raises:
        TypeError: If either s or c is not a string

    Note: Both deletion and palindrome checks are case-sensitive.
    """
    # Check if both inputs are strings
    if not isinstance(s, str):
        raise TypeError("First argument must be a string")
    if not isinstance(c, str):
        raise TypeError("Second argument must be a string")

    # Create a set of characters to delete for efficient lookup
    chars_to_delete = set(c)

    # Remove characters that are present in c from s
    new_string = ''.join(char for char in s if char not in chars_to_delete)

    # Check if the resulting string is a palindrome (case-sensitive)
    is_palindrome = new_string == new_string[::-1]

    return (new_string, is_palindrome)