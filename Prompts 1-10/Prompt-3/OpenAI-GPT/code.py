def minPath(grid, k):
    from heapq import heappush, heappop

    n = len(grid)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    heap = []
    # Push all starting positions
    for i in range(n):
        for j in range(n):
            heappush(heap, ([grid[i][j]], i, j))

    while heap:
        path, x, y = heappop(heap)
        if len(path) == k:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_path = path + [grid[nx][ny]]
                heappush(heap, (new_path, nx, ny))

    return []