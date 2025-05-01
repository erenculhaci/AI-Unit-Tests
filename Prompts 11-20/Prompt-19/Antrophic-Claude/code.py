# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # Convert the string to a float
    num = float(value)
    
    # Get the fractional part
    fractional_part = abs(num) - int(abs(num))
    
    # If the fractional part is exactly 0.5, round away from zero
    if fractional_part == 0.5:
        if num > 0:
            return int(num) + 1  # Round up for positive numbers
        else:
            return int(num) - 1  # Round down for negative numbers
    
    # Otherwise, use the built-in round function
    # (which rounds to nearest even integer when equidistant)
    return round(num)