# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def eat(number, need, remaining):
    # Type checks
    if not all(isinstance(x, int) for x in (number, need, remaining)):
        raise TypeError("All inputs must be integers.")
    
    # Disallow negative numbers
    if number < 0 or need < 0 or remaining < 0:
        raise ValueError("Inputs must be non-negative integers.")
    
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]
