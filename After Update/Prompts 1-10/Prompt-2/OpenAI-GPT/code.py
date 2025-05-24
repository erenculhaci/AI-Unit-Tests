# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def pluck(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(val, int) and not isinstance(val, bool) for val in arr):
        raise TypeError("All elements in the list must be non-boolean integers")

    even_nodes = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    smallest_even = min(even_nodes, key=lambda x: (x[0], x[1]))
    return [smallest_even[0], smallest_even[1]]

