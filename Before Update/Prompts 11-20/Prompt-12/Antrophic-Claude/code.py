# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    coordinates = []
    
    # Iterate through each row
    for row_idx, row in enumerate(lst):
        # Find all occurrences of x in the current row
        row_coordinates = [(row_idx, col_idx) for col_idx, val in enumerate(row) if val == x]
        
        # Sort coordinates within the same row by column in descending order
        row_coordinates.sort(key=lambda coord: coord[1], reverse=True)
        
        # Add the sorted coordinates to the result
        coordinates.extend(row_coordinates)
    
    # The coordinates are already sorted by row in ascending order
    # due to the iteration order, so no additional sorting is needed
    
    return coordinates