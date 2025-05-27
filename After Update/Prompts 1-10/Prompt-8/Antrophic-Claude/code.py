# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def eat(number, need, remaining):
    # Type validation - check if all inputs are integers (but allow bool since bool is subclass of int)
    if not isinstance(number, int) or not isinstance(need, int) or not isinstance(remaining, int):
        raise TypeError("All inputs must be integers")
    
    # Value validation - check for negative values
    if number < 0:
        raise ValueError("Number of eaten carrots cannot be negative")
    if need < 0:
        raise ValueError("Number of needed carrots cannot be negative")
    if remaining < 0:
        raise ValueError("Number of remaining carrots cannot be negative")
    
    # Check if there are enough remaining carrots
    if remaining >= need:
        # If there are enough carrots, eat what you need
        total_eaten = number + need
        carrots_left = remaining - need
    else:
        # If there aren't enough carrots, eat all remaining carrots
        total_eaten = number + remaining
        carrots_left = 0
    
    return [total_eaten, carrots_left]