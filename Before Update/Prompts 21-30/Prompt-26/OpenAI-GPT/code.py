# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def reverse_delete(s, c):
    filtered = ''.join(ch for ch in s if ch not in c)
    return (filtered, filtered == filtered[::-1])
