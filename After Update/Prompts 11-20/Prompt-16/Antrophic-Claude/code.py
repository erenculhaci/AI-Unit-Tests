# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []
    
    for num in x:
        # Convert number to string to check each digit
        num_str = str(num)
        
        # Check if all digits are odd
        all_digits_odd = True
        for digit in num_str:
            if int(digit) % 2 == 0:  # If digit is even
                all_digits_odd = False
                break
        
        # If all digits are odd, add to result
        if all_digits_odd:
            result.append(num)
    
    # Sort the result in increasing order
    return sorted(result)