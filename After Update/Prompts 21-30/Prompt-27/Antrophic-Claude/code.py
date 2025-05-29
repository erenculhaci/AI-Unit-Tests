def decimal_to_binary(n):
    """
    Converts a non-negative integer to its binary representation wrapped in "db" format.

    Args:
        n: A non-negative integer to convert to binary

    Returns:
        str: Binary representation in format "db<binary>db"

    Raises:
        TypeError: If input is not an integer
        ValueError: If input is a negative integer
    """
    # Check if input is an integer
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")

    # Check if input is non-negative
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Convert to binary (remove '0b' prefix from bin() function)
    binary_representation = bin(n)[2:]

    # Wrap with "db" at both ends
    return f"db{binary_representation}db"