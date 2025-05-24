# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def sorted_list_sum(lst):
    """
    Accepts a list of strings as a parameter, deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order.
    
    Args:
        lst (list): A list of strings
        
    Returns:
        list: A list of strings where all strings have even length, sorted by length
              and then alphabetically if lengths are equal
    """
    # Filter out strings with odd lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list first by length, then alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    return sorted_strings