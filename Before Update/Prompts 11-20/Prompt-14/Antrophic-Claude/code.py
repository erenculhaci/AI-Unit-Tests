# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ""
    
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        # Extract the suffix starting at position i-1
        suffix = string[i-1:]
        
        # Check if this suffix is a palindrome
        if suffix == suffix[::-1]:
            # Get the prefix that comes before the palindromic suffix
            prefix = string[:i-1]
            # Append the reverse of the prefix to the original string
            return string + prefix[::-1]
    
    # If no palindromic suffix is found (which should never happen 
    # as a single character is always a palindrome), return the string
    # with its reverse (except the first character) appended
    return string + string[1:][::-1]