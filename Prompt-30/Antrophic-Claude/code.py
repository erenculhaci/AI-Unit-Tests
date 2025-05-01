def words_in_sentence(sentence):
    """
    Returns a string containing only the words from the input sentence
    whose lengths are prime numbers, maintaining the original order.
    
    Args:
        sentence (str): A string containing words separated by spaces
        
    Returns:
        str: A string with only the words whose lengths are prime numbers
    """
    # Helper function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    # Split the sentence into words
    words = sentence.split()
    
    # Filter words whose lengths are prime
    prime_length_words = [word for word in words if is_prime(len(word))]
    
    # Join the filtered words back into a string
    result = " ".join(prime_length_words)
    
    return result