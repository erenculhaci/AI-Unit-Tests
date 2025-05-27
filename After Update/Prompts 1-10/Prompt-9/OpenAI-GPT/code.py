# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Supports int, float, and complex numbers.
    """
    if not isinstance(xs, (list, tuple)):
        raise TypeError("xs must be a list or tuple of coefficients.")
    if not isinstance(x, (int, float, complex)):
        raise TypeError("x must be a number (int, float, or complex).")

    for coeff in xs:
        if not isinstance(coeff, (int, float, complex)):
            raise TypeError("All elements of xs must be int, float, or complex.")

    result = 0
    for power, coeff in enumerate(xs):
        result += coeff * (x ** power)
    return result

