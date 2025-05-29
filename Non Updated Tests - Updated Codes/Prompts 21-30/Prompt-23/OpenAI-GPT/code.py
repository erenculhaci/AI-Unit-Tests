# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def solve(n):
    if type(n) is not int:
        raise TypeError("Input must be an integer.")
    if n < 0 or n > 10000:
        raise ValueError("Input must be between 0 and 10000 inclusive.")

    digit_sum = sum(int(d) for d in str(n))
    return bin(digit_sum)[2:]
