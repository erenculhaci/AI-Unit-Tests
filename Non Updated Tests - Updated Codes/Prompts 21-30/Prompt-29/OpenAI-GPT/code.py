# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Input validation
    for interval in (interval1, interval2):
        if not isinstance(interval, tuple):
            raise TypeError("Both inputs must be tuples.")
        if len(interval) != 2:
            raise ValueError("Each interval must contain exactly two elements.")
        if not all(isinstance(i, int) for i in interval):
            raise TypeError("Interval elements must be integers.")

    # Normalize interval order
    a1, a2 = sorted(interval1)
    b1, b2 = sorted(interval2)

    # Compute intersection
    start = max(a1, b1)
    end = min(a2, b2)

    if start >= end:
        return "NO"

    length = end - start
    return "YES" if is_prime(length) else "NO"
