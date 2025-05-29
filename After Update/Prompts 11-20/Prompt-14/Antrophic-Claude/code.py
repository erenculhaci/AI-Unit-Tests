# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def make_palindrome(string: str) -> str:
    if not string:
        return ""
    for i in range(len(string)):
        to_add = string[:i][::-1]
        candidate = string + to_add
        if candidate == candidate[::-1]:
            return candidate
    return string + string[:-1][::-1]
