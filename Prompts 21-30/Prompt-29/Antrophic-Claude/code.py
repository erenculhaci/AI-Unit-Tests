def intersection(interval1, interval2):
    """
    Determines if the length of intersection between two intervals is a prime number.
    
    Args:
        interval1 (tuple): First interval as (start, end)
        interval2 (tuple): Second interval as (start, end)
        
    Returns:
        str: "YES" if intersection length is prime, "NO" otherwise
    """
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
    
    # Extract start and end points of the intervals
    start1, end1 = interval1
    start2, end2 = interval2
    
    # Calculate the intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    
    # If intervals don't intersect
    if intersection_start > intersection_end:
        return "NO"
    
    # Calculate the length of intersection (inclusive of both endpoints)
    intersection_length = intersection_end - intersection_start
    
    # Check if the length is prime
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"