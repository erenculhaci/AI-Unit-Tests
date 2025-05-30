# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def pluck(arr):
    even_nodes = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    smallest_even = min(even_nodes, key=lambda x: (x[0], x[1]))
    return [smallest_even[0], smallest_even[1]]
