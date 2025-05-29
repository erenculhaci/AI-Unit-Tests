def words_in_sentence(sentence):
    """
    Returns words from a sentence that have a prime number of characters.

    Args:
        sentence (str): Input sentence containing words separated by spaces

    Returns:
        str: String containing prime-length words in original order, space-separated

    Raises:
        TypeError: If input is not a string (via AttributeError when calling split())
    """

    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        # Check odd divisors up to sqrt(n)
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_alphabetic_only(word):
        """Check if word contains only alphabetic characters."""
        return word.isalpha()

    # This will raise AttributeError for non-string inputs
    words = sentence.split()

    # Filter words that are alphabetic only and have prime length
    prime_words = []
    for word in words:
        if is_alphabetic_only(word) and is_prime(len(word)):
            prime_words.append(word)

    # Join the filtered words with spaces
    return " ".join(prime_words)