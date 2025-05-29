def sort_array(array):
    """
    Sorts a copy of the array based on the sum of first and last elements:
    - Ascending if the sum is odd
    - Descending if the sum is even

    Raises:
    - ValueError if any element is negative
    - TypeError if any element is not an int
    """
    if not isinstance(array, list):
        raise TypeError("Input must be a list")

    for x in array:
        if not isinstance(x, int):
            raise TypeError("All elements must be integers")
        if x < 0:
            raise ValueError("All elements must be non-negative")

    if not array:
        return []

    result = array.copy()

    if len(array) == 1:
        return result

    sum_first_last = array[0] + array[-1]

    if sum_first_last % 2 == 1:
        result.sort()
    else:
        result.sort(reverse=True)

    return result
