# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def get_odd_collatz(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    odds = set()
    while n != 1:
        if n % 2 == 1:
            odds.add(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    odds.add(1)

    # Return sorted list with 1 first
    return [1] + sorted(x for x in odds if x != 1)

