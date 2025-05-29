def intersection(interval1, interval2):
    """
    Determines whether two intervals intersect and if the overlapping length is prime.

    Args:
        interval1: A tuple of two integers (start, end)
        interval2: A tuple of two integers (start, end)

    Returns:
        str: "YES" if intervals overlap and overlapping length is prime, "NO" otherwise

    Raises:
        TypeError: If inputs are not tuples or elements are not integers
        ValueError: If tuples don't have exactly 2 elements
    """

    def validate_interval(interval):
        """Validate that the interval is a tuple of two integers."""
        if not isinstance(interval, tuple):
            raise TypeError("Input must be a tuple")

        if len(interval) != 2:
            raise ValueError("Tuple must have exactly 2 elements")

        for element in interval:
            if not isinstance(element, int) or isinstance(element, bool):
                raise TypeError("Tuple elements must be integers")

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

    # Validate both intervals
    validate_interval(interval1)
    validate_interval(interval2)

    # Normalize intervals so that start <= end
    start1, end1 = min(interval1), max(interval1)
    start2, end2 = min(interval2), max(interval2)

    # Find the intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    # Check if intervals actually intersect
    if intersection_start >= intersection_end:
        return "NO"

    # Calculate the length of the intersection
    intersection_length = intersection_end - intersection_start

    # Check if the length is prime
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"