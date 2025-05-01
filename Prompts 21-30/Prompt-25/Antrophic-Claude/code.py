# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def is_palindrome(text: str):
    """
    Checks if the given string is a palindrome
    
    Args:
        text (str): The input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # An empty string is considered a palindrome
    if not text:
        return True
    
    # Compare the string with its reverse
    return text == text[::-1]