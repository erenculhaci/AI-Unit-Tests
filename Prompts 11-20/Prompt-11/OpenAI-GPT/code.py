# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def max_fill(grid, capacity):
    import math
    """
    Calculate the number of times buckets need to be lowered to empty the wells.
    
    Args:
    grid (list of list of int): A 2D grid representing the wells.
    capacity (int): The capacity of each bucket.
    
    Returns:
    int: The number of times buckets need to be lowered.
    """
    total_water_units = 0

    # Calculate the total number of water units in the grid
    for row in grid:
        total_water_units += sum(row)

    # Calculate the number of bucket trips needed
    bucket_trips = math.ceil(total_water_units / capacity)

    return bucket_trips