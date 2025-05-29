# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Invalid input (non-integers, negative numbers, or non-list) raises ValueError.
    '''
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")

    counts = {}
    for num in lst:
        if not isinstance(num, int):
            raise ValueError("All elements must be integers.")
        if num < 0:
            raise ValueError("Negative numbers are not allowed.")
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > 2:
            return False

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False

    return True
