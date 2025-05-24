# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def minPath(grid, k):
    from heapq import heappush, heappop

    if not isinstance(grid, list):
        raise TypeError("Grid must be a list of lists")
    if len(grid) == 0:
        return []
    n = len(grid)
    for row in grid:
        if not isinstance(row, list):
            raise TypeError("Grid must be a list of lists")
        if len(row) != n:
            raise TypeError("Grid must be square (all rows same length)")
        for val in row:
            if not isinstance(val, int):
                raise TypeError("Grid values must be integers")

    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k <= 0:
        return []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heap = []

    for i in range(n):
        for j in range(n):
            heappush(heap, ([grid[i][j]], i, j, {(i, j)}))

    while heap:
        path, x, y, visited = heappop(heap)
        if len(path) == k:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                new_path = path + [grid[nx][ny]]
                new_visited = visited.copy()
                new_visited.add((nx, ny))
                heappush(heap, (new_path, nx, ny, new_visited))

    return []