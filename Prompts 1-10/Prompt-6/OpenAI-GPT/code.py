def get_odd_collatz(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    sequence = []
    while n != 1:
        if n % 2 == 1:
            sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)  # Ensure 1 is included
    return sorted(sequence)
