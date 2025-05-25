# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def maximum(arr, k):
    # Input validation
    if arr is None:
        raise TypeError("Array cannot be None")
    
    if not isinstance(arr, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    if k is None:
        raise TypeError("k cannot be None")
    
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError("k must be an integer")
    
    if k < 0:
        raise ValueError("k cannot be negative")
    
    # Check for invalid elements in the array
    for element in arr:
        if element is None:
            raise TypeError("Array cannot contain None values")
        if isinstance(element, str):
            raise TypeError("Array cannot contain string values")
        # Allow numeric types (int, float, bool - which is treated as int)
        if not isinstance(element, (int, float, bool)):
            raise TypeError("Array elements must be numeric")
    
    # Handle edge case where k is 0
    if k == 0:
        return []
    
    # Handle case where k is greater than array length
    if k > len(arr):
        k = len(arr)
    
    # Sort the array
    sorted_arr = sorted(arr)
    
    # Return the last k elements (the maximum k numbers)
    return sorted_arr[-k:]