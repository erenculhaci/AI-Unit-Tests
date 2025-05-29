def sorted_list_sum(lst):
    """
    Returns a sorted list of only the strings with even lengths.

    Args:
        lst: A list of strings

    Returns:
        A list of strings with even lengths, sorted first by length
        (ascending) and then alphabetically for strings of the same length.

    Raises:
        TypeError: If input is not a list or if any element is not a string.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    # Check if all elements are strings
    for element in lst:
        if not isinstance(element, str):
            raise TypeError("All elements must be strings")

    # Filter strings with even lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]

    # Sort by length first, then alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))

    return sorted_strings