# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def maximum(arr, k):
    if not isinstance(arr, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    
    if k < 0:
        raise ValueError("k must be non-negative.")

    if k == 0:
        return []

    try:
        top_k = sorted(arr, reverse=True)[:k]
        return sorted(top_k)
    except TypeError as e:
        raise TypeError("Elements in the list must be comparable.") from e
