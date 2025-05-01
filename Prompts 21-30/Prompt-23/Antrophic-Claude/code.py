def solve(N):
    """
    Given a positive integer N, returns the total sum of its digits in binary.
    
    Args:
        N (int): A positive integer
        
    Returns:
        str: Binary representation of the sum of digits of N
    """
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(N))
    
    # Convert the sum to binary (removing '0b' prefix)
    binary_sum = bin(digit_sum)[2:]
    
    return binary_sum