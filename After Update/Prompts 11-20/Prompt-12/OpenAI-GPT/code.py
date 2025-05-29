# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def get_row(lst, x):
    """
    Finds all occurrences of `x` in a 2D jagged list and returns a list of (row, column) coordinates.
    Sorts results by row (ascending) and column (descending).
    """
    if lst is None:
        raise TypeError("Input list cannot be None")
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not isinstance(x, int):
        raise TypeError("Target value must be an integer")

    coordinates = []

    for row_idx, row in enumerate(lst):
        if not isinstance(row, list):
            raise TypeError(f"Row at index {row_idx} is not a list")

        row_coordinates = []
        for col_idx, val in enumerate(row):
            # Nested lists are not allowed; raise an error immediately
            if isinstance(val, list):
                raise TypeError(f"Nested list found at position [{row_idx}, {col_idx}]")
            if isinstance(val, int) and val == x:
                row_coordinates.append((row_idx, col_idx))

        # Sort coordinates within the same row by column descending
        row_coordinates.sort(key=lambda t: t[1], reverse=True)
        coordinates.extend(row_coordinates)

    return coordinates
