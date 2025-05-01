# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    
    Parameters:
    xs -- list of coefficients, where xs[i] is the coefficient for x^i
    x -- the point at which to evaluate the polynomial
    
    Returns:
    float -- the result of evaluating the polynomial at point x
    """
    result = 0
    for i, coefficient in enumerate(xs):
        result += coefficient * (x ** i)
    return result