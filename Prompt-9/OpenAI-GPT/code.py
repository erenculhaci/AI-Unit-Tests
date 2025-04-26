def poly(xs: list, x: float):
    """
    Evaluates a polynomial with coefficients xs at point x.
    Computes xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    result = 0
    for power, coeff in enumerate(xs):
        result += coeff * (x ** power)
    return result
