# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import math

def max_fill(grid, capacity):
    """
    Calculate the minimum number of trips required to empty a grid of water wells.
    
    Args:
        grid: A 2D list representing water levels in wells
        capacity: The capacity of the bucket to carry water
        
    Returns:
        The minimum number of trips required to empty all wells
    """
    if not isinstance(grid, list):
        raise TypeError("Grid must be a list")
    if not isinstance(capacity, int):
        raise TypeError("Capacity must be an integer")
    if capacity <= 0:
        raise ValueError("Capacity must be a positive integer")

    # Validate grid structure
    if len(grid) > 0:
        row_length = len(grid[0])
        for row in grid:
            if not isinstance(row, list):
                raise TypeError("Each row in the grid must be a list")
            if len(row) != row_length:
                raise ValueError("All rows in the grid must have the same length")
            for cell in row:
                if not isinstance(cell, int):
                    raise TypeError("Grid cells must contain integers")
                if cell < 0:
                    raise ValueError("Grid cells cannot contain negative values")

    # Flatten the grid to consider all cells together
    all_cells = []
    for row in grid:
        all_cells.extend(row)
    
    # Filter out cells with no water
    water_cells = [cell for cell in all_cells if cell > 0]
    
    # If there's no water, no trips needed
    if not water_cells:
        return 0
    
    # Calculate total water
    total_water = sum(water_cells)
    
    # Calculate minimum trips needed, considering optimal path
    # Each trip can carry at most 'capacity' amount of water
    return math.ceil(total_water / capacity)