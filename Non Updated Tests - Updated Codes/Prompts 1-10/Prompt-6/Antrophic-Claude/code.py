# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def get_odd_collatz(n):
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle boolean case (since bool is a subclass of int in Python)
    if isinstance(n, bool) and n is False:
        raise ValueError("Input must be a positive integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Generate the full Collatz sequence
    sequence = [n]
    current = n
    
    while current != 1:
        if current % 2 == 0:  # If current is even
            current = current // 2
        else:  # If current is odd
            current = 3 * current + 1
        sequence.append(current)
    
    # Filter for odd numbers and sort them
    odd_numbers = [num for num in sequence if num % 2 == 1]
    return sorted(odd_numbers)