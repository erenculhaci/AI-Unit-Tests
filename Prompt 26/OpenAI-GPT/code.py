def reverse_delete(s, c):
    filtered = ''.join(ch for ch in s if ch not in c)
    return (filtered, filtered == filtered[::-1])
