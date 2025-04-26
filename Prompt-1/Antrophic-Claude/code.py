def move_one_ball(arr):
    """
    Determine if it's possible to sort the array in non-decreasing order
    by performing any number of right shift operations.
    
    Args:
        arr (list): A list of unique integers
        
    Returns:
        bool: True if sorting is possible through right shifts, False otherwise
    """
    # Empty arrays are considered sorted
    if not arr:
        return True
    
    n = len(arr)
    
    # Find the index of the minimum element
    min_idx = arr.index(min(arr))
    
    # Check if the array is sorted in rotated form
    # This means: arr[min_idx:] + arr[:min_idx] should be sorted
    rotated = arr[min_idx:] + arr[:min_idx]
    
    # Check if the rotated array is sorted in non-decreasing order
    for i in range(1, n):
        if rotated[i] < rotated[i-1]:
            return False
    
    return True