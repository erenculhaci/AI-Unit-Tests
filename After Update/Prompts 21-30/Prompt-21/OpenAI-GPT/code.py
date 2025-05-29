# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def sorted_list_sum(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    for item in lst:
        if not isinstance(item, str):
            raise TypeError("All elements of the list must be strings.")

    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    return sorted(even_length_strings, key=lambda x: (len(x), x))
