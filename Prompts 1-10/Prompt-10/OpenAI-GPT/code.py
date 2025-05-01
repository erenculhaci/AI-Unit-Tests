# code.py

def find_zero(xs: list):
    """ xs are coefficients of a polynomial from constant to higher degrees.
    find_zero finds x such that poly(x) = 0.
    """
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    if not any(xs):
        raise ValueError("At least one coefficient must be nonzero.")

    import numpy as np

    xs_reversed = xs[::-1]  # Reverse the list to match np.roots expectations
    roots = np.roots(xs_reversed)
    real_roots = [r.real for r in roots if np.isreal(r)]

    if not real_roots:
        raise ValueError("No real roots found.")

    return real_roots[0]
