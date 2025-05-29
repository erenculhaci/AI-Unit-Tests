# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all 
    elements that haven't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    def has_even_digit(num):
        """Helper function to check if a number contains any even digit."""
        return any(int(digit) % 2 == 0 for digit in str(num))
    
    # Filter out numbers that contain even digits
    result = [num for num in x if not has_even_digit(num)]
    
    # Return the sorted result
    return sorted(result)