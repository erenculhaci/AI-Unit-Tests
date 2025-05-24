# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def pluck(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Validate all elements are integers
    for i, element in enumerate(arr):
        if not isinstance(element, int) or isinstance(element, bool):
            raise TypeError(f"All elements must be integers, found {type(element).__name__} at index {i}")
    
    smallest_even = float('inf')
    smallest_index = -1
    
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_index = i
    
    if smallest_index == -1: 
        return []
    
    return [smallest_even, smallest_index]