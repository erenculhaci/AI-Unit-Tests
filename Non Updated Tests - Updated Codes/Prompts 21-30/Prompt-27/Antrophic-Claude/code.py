def get_closest_vowel(word):
    """
    Returns the rightmost vowel in a word that is surrounded by consonants on both sides.

    Args:
        word (str): The input word to analyze

    Returns:
        str: The rightmost surrounded vowel (case preserved), or "" if no such vowel exists

    Raises:
        TypeError: If the input is not a string
    """
    # Check if input is a string
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    # Handle empty string or strings with length < 3
    if len(word) < 3:
        return ""

    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')

    # Iterate from right to left to find the rightmost surrounded vowel
    for i in range(len(word) - 2, 0, -1):  # Start from second-to-last char, go to second char
        current_char = word[i]
        left_char = word[i - 1]
        right_char = word[i + 1]

        # Check if current character is a vowel and surrounded by consonants
        if (current_char in vowels and
                left_char not in vowels and
                right_char not in vowels):
            return current_char

    # No surrounded vowel found
    return ""