# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def move_one_ball(arr):
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    for element in arr:
        if not isinstance(element, int) or isinstance(element, bool):
            raise TypeError("All elements must be integers")
    
    # Empty arrays are considered sorted
    if not arr:
        return True
    
    n = len(arr)
    
    # Single element is always sorted
    if n == 1:
        return True
    
    # Find the index of the minimum element
    min_val = min(arr)
    min_idx = arr.index(min_val)
    
    # Check if the array is sorted in rotated form
    # This means: arr[min_idx:] + arr[:min_idx] should be sorted
    rotated = arr[min_idx:] + arr[:min_idx]
    
    # Check if the rotated array is sorted in non-decreasing order
    for i in range(1, n):
        if rotated[i] < rotated[i-1]:
            return False
    
    return True