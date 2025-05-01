# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Return empty array if input is empty
    if not array:
        return []
    
    # Create a copy of the array to avoid modifying the original
    result = array.copy()
    
    # If array has only one element, return it (no sorting needed)
    if len(array) == 1:
        return result
    
    # Calculate sum of first and last values
    sum_first_last = array[0] + array[-1]
    
    # Sort in ascending order if sum is odd
    if sum_first_last % 2 == 1:
        result.sort()
    # Sort in descending order if sum is even
    else:
        result.sort(reverse=True)
    
    return result