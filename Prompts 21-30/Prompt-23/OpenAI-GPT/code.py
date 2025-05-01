# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def solve(N):
    digit_sum = sum(int(d) for d in str(N))
    return bin(digit_sum)[2:]
