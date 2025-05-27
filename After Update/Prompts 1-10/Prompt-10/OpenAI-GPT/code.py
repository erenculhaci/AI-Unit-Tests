# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
 
import numpy as np
import math

def find_zero(coeffs):
    # 1. Check input type, raise AttributeError if not list
    if not isinstance(coeffs, list):
        raise AttributeError("Input must be a list of coefficients.")

    # 2. Convert bools to int
    coeffs = [int(c) if isinstance(c, bool) else c for c in coeffs]

    # 3. Check all are numbers
    if not all(isinstance(c, (int, float)) for c in coeffs):
        raise TypeError("All coefficients must be numbers.")

    # 4. Check NaN or Inf → raise TypeError (per test expectation)
    if any(math.isnan(c) or math.isinf(c) for c in coeffs):
        raise TypeError("Coefficients must not contain NaN or infinity.")

    # 5. Check empty list or all zeros (invalid)
    if len(coeffs) == 0 or all(c == 0 for c in coeffs):
        raise ValueError("Polynomial cannot be empty or all zeros.")

    # 6. Find last non-zero coefficient index
    last_nonzero_idx = -1
    for i in reversed(range(len(coeffs))):
        if coeffs[i] != 0:
            last_nonzero_idx = i
            break

    if last_nonzero_idx != len(coeffs) - 1:
        # Trailing zeros found after last non-zero coefficient
        raise ValueError("Polynomial cannot have trailing zeros in coefficients.")

    # 7. Remove leading zeros but keep at least two coefficients for degree 1 polynomial
    while len(coeffs) > 1 and coeffs[0] == 0:
        coeffs.pop(0)

    # 8. After trimming leading zeros, length must be ≥ 2 (degree ≥ 1)
    if len(coeffs) < 2:
        raise ValueError("Polynomial must have at least degree 1.")

    # 9. Use numpy roots (coefficients reversed for numpy poly format)
    roots = np.roots(coeffs[::-1])

    # 10. Return first real root found
    for r in roots:
        if np.isreal(r):
            return float(np.real(r))

    raise ValueError("No real roots found.")
