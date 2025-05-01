# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def get_closest_vowel(word):
    """
    Find the closest vowel that stands between two consonants from the right side of the word.
    
    Args:
        word (str): The input word (case sensitive)
        
    Returns:
        str: The closest vowel meeting the condition, or empty string if none found
    """
    # Define vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Word needs at least 3 characters for a vowel to be between two consonants
    if len(word) < 3:
        return ""
    
    # Start from the right side (excluding the last character)
    for i in range(len(word) - 2, 0, -1):
        current_char = word[i]
        prev_char = word[i - 1]
        next_char = word[i + 1]
        
        # Check if current character is a vowel
        if current_char in vowels:
            # Check if characters on both sides are consonants
            if prev_char not in vowels and next_char not in vowels:
                return current_char
    
    # If no vowel is found meeting the conditions
    return ""