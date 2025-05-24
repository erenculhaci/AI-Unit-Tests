# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]  # Remove '0b' prefix
    return f"db{binary_str}db"
