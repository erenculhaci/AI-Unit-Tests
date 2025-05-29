def solve(n: int) -> str:
    """
    Takes a single integer input n and returns a string representing the
    binary form of the sum of its digits.

    Args:
        n: An integer where 0 ≤ n ≤ 10000

    Returns:
        A string representing the binary form of the sum of digits of n

    Raises:
        TypeError: If the input is not an integer
        ValueError: If the input is less than 0 or greater than 10000
    """
    # Check if input is an integer
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer.")

    # Check if input is within valid range
    if n < 0 or n > 10000:
        raise ValueError("Input must be between 0 and 10000 inclusive.")

    # Calculate sum of digits
    digit_sum = 0
    temp = n

    # Handle the special case of 0
    if n == 0:
        digit_sum = 0
    else:
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10

    # Convert sum to binary and remove '0b' prefix
    binary_representation = bin(digit_sum)[2:]

    return binary_representation