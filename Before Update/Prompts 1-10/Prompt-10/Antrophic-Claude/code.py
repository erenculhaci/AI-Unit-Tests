# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check if length of coefficient list is even
    if len(xs) % 2 != 0:
        raise ValueError("Coefficient list must have an even number of elements")
    
    # Check if the highest degree coefficient is non-zero
    if xs[-1] == 0:
        raise ValueError("Highest degree coefficient must be non-zero")
    
    # For simple case: 1 + 2x = 0 -> x = -1/2
    if len(xs) == 2:
        return -xs[0] / xs[1]
    
    # For more complex polynomials, use the Newton-Raphson method
    def polynomial(x):
        result = 0
        for i, coef in enumerate(xs):
            result += coef * (x ** i)
        return result
    
    def derivative(x):
        result = 0
        for i, coef in enumerate(xs[1:], 1):
            result += i * coef * (x ** (i-1))
        return result
    
    # Start with an initial guess
    x = 0
    
    # Iterate until convergence (or max iterations)
    max_iterations = 100
    tolerance = 1e-10
    
    for _ in range(max_iterations):
        p = polynomial(x)
        
        # If we're close enough to zero, return the result
        if abs(p) < tolerance:
            return x
        
        dp = derivative(x)
        
        # Avoid division by zero
        if abs(dp) < 1e-10:
            x += 0.1  # Perturb x if derivative is close to zero
            continue
        
        # Newton-Raphson update
        x_new = x - p / dp
        
        # Check for convergence
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new
    
    # If we exit the loop, we've reached max iterations
    return x