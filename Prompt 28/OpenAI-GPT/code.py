def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]  # Remove '0b' prefix
    return f"db{binary_str}db"
