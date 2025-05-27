# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def poly(xs: list, x: float) -> float:
    # Check if xs is None
    if xs is None:
        raise TypeError("Coefficients cannot be None")
    
    # Check if xs is a dictionary or generator
    if isinstance(xs, dict):
        raise TypeError("Coefficients cannot be a dictionary")
    
    # Check for generator types
    if hasattr(xs, '__iter__') and hasattr(xs, '__next__'):
        raise TypeError("Coefficients cannot be a generator")
    
    # Check if x is a string
    if isinstance(x, str):
        raise TypeError("x cannot be a string")
    
    result = 0
    try:
        for i, coefficient in enumerate(xs):
            # Check for None values inside the list
            if coefficient is None:
                raise TypeError("Coefficient cannot be None")
            
            # Check for string values inside the list
            if isinstance(coefficient, str):
                raise TypeError("Coefficient cannot be a string")
            
            result += coefficient * (x ** i)
    except TypeError as e:
        # Re-raise TypeError if it's one we explicitly raised
        if "cannot be" in str(e):
            raise
        raise TypeError("Invalid input type")
    
    return result