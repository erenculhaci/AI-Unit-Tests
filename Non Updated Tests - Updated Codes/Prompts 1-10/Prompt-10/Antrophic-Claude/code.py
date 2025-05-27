# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import math
import numpy as np

def find_zero(coeffs):
    # Check if input is a list
    if not isinstance(coeffs, list):
        raise AttributeError("Input must be a list")
    
    # Check if list is empty
    if len(coeffs) == 0:
        raise ValueError("Coefficient list cannot be empty")
    
    # Check if length is even
    if len(coeffs) % 2 != 0:
        raise ValueError("Coefficient list must have an even number of elements")
    
    # Check coefficient types and values
    for coeff in coeffs:
        # Check for boolean (must come before numeric check since bool is subclass of int)
        if isinstance(coeff, bool):
            raise ValueError("Boolean coefficients are not allowed")
        
        # Check if coefficient is numeric
        if not isinstance(coeff, (int, float)):
            raise TypeError("All coefficients must be numeric (int or float)")
        
        # Check for NaN or infinity
        if math.isnan(coeff) or math.isinf(coeff):
            raise TypeError("Coefficients cannot be NaN or infinite")
    
    # Check for all zero coefficients
    if all(coeff == 0 for coeff in coeffs):
        raise ValueError("All coefficients cannot be zero")
    
    # Check for trailing zeros (highest degree coefficient must be non-zero)
    if coeffs[-1] == 0:
        raise ValueError("Trailing zeros are not allowed - highest degree coefficient must be non-zero")
    
    # Trim leading zeros
    while len(coeffs) > 2 and coeffs[0] == 0:
        coeffs = coeffs[1:]
    
    # Check minimum degree requirement (at least 2 coefficients after trimming)
    if len(coeffs) < 2:
        raise ValueError("Polynomial must have degree at least 1")
    
    # For linear case: ax + b = 0 -> x = -b/a
    if len(coeffs) == 2:
        if coeffs[1] == 0:
            raise ValueError("Linear coefficient cannot be zero")
        return -coeffs[0] / coeffs[1]
    
    # For higher degree polynomials, use numpy.roots for better numerical stability
    try:
        # Reverse coefficients for numpy (numpy expects highest degree first)
        numpy_coeffs = coeffs[::-1]
        roots = np.roots(numpy_coeffs)
        
        # Find real roots
        real_roots = []
        for root in roots:
            if np.isreal(root):
                real_root = float(np.real(root))
                # Verify it's actually a root by checking polynomial value
                if abs(evaluate_polynomial(coeffs, real_root)) < 1e-10:
                    real_roots.append(real_root)
        
        if not real_roots:
            raise ValueError("No real roots found")
        
        # Return the first real root found
        return real_roots[0]
        
    except Exception as e:
        if "No real roots found" in str(e):
            raise e
        # Fallback to Newton-Raphson if numpy fails
        return newton_raphson_method(coeffs)

def evaluate_polynomial(coeffs, x):
    """Evaluate polynomial at given x value"""
    result = 0
    for i, coeff in enumerate(coeffs):
        result += coeff * (x ** i)
    return result

def evaluate_derivative(coeffs, x):
    """Evaluate derivative of polynomial at given x value"""
    result = 0
    for i, coeff in enumerate(coeffs[1:], 1):
        result += i * coeff * (x ** (i-1))
    return result

def newton_raphson_method(coeffs):
    """Fallback Newton-Raphson method for finding roots"""
    # Try multiple starting points
    starting_points = [0, 1, -1, 10, -10, 0.1, -0.1]
    
    for start_x in starting_points:
        try:
            x = start_x
            max_iterations = 1000
            tolerance = 1e-12
            
            for iteration in range(max_iterations):
                p = evaluate_polynomial(coeffs, x)
                
                # Check if we found a root
                if abs(p) < tolerance:
                    return x
                
                dp = evaluate_derivative(coeffs, x)
                
                # Avoid division by zero
                if abs(dp) < 1e-15:
                    break  # Try next starting point
                
                # Newton-Raphson update
                x_new = x - p / dp
                
                # Check for convergence
                if abs(x_new - x) < tolerance:
                    # Verify it's actually a root
                    if abs(evaluate_polynomial(coeffs, x_new)) < 1e-10:
                        return x_new
                
                x = x_new
                
                # Prevent divergence
                if abs(x) > 1e10:
                    break
                    
        except (OverflowError, ZeroDivisionError):
            continue
    
    # If all starting points fail, raise error
    raise ValueError("No real roots found")