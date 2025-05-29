def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    # Check if input is a list
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")

    # Check that all elements are integers and non-negative
    for val in lst:
        if not isinstance(val, int):
            raise ValueError("All elements must be integers")
        if val < 0:
            raise ValueError("Negative values are not allowed")

    # Check ascending order
    if lst != sorted(lst):
        return False

    # Check duplicate count > 2
    for num in set(lst):
        if lst.count(num) > 2:
            return False

    return True
