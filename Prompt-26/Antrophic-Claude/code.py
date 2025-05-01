def reverse_delete(s, c):
    """
    Delete all characters in s that match any character in c, 
    then check if the result is a palindrome.
    
    Args:
        s (str): The input string
        c (str): Characters to delete
        
    Returns:
        tuple: (result_string, is_palindrome)
    """
    # Delete characters from s that are in c
    result = ''.join(char for char in s if char not in c)
    
    # Check if the result is a palindrome
    is_palindrome = result == result[::-1]
    
    return (result, is_palindrome)