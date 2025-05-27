# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def minPath(grid, k):
    # Input validation
    if not isinstance(grid, list):
        raise TypeError("Grid must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Handle edge cases
    if k <= 0:
        return []
    
    if not grid:  # Empty grid
        return []
    
    # Validate grid structure and content
    rows = len(grid)
    if rows == 0:
        return []
    
    # Check if all rows are lists and have the same length
    if not all(isinstance(row, list) for row in grid):
        raise TypeError("All grid rows must be lists")
    
    cols = len(grid[0])
    if not all(len(row) == cols for row in grid):
        raise TypeError("All grid rows must have the same length")
    
    # Check if all elements are integers
    for i in range(rows):
        for j in range(cols):
            if not isinstance(grid[i][j], int):
                raise TypeError("All grid elements must be integers")
    
    # If k is greater than the maximum possible path length, return empty list
    max_possible_length = rows * cols
    if k > max_possible_length:
        return []
    
    # For single cell grid, only k=1 is possible
    if rows == 1 and cols == 1:
        if k == 1:
            return [grid[0][0]]
        else:
            return []
    
    # Define valid neighbor directions (up, right, down, left)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Find the lexicographically smallest path of length k
    best_path = None
    
    def dfs(row, col, path, length, visited):
        nonlocal best_path
        
        # If we've reached the desired path length
        if length == k:
            if best_path is None or path < best_path:
                best_path = path.copy()
            return
        
        # Pruning: if current path is already worse than best found
        if best_path is not None and path >= best_path[:length]:
            return
        
        # Get all valid neighbors and their values
        neighbors = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                neighbors.append((grid[new_row][new_col], new_row, new_col))
        
        # Sort neighbors by value to try smaller values first
        neighbors.sort()
        
        # Explore each neighbor
        for val, new_row, new_col in neighbors:
            path.append(val)
            visited.add((new_row, new_col))
            dfs(new_row, new_col, path, length + 1, visited)
            visited.remove((new_row, new_col))
            path.pop()
    
    # Try starting from each cell in the grid
    for i in range(rows):
        for j in range(cols):
            visited = {(i, j)}
            dfs(i, j, [grid[i][j]], 1, visited)
    
    return best_path if best_path is not None else []