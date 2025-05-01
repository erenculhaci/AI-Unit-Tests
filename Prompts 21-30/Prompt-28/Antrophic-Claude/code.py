# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def decimal_to_binary(decimal):
    """
    Converts a decimal number to binary format with 'db' prefix and suffix.
    
    Args:
        decimal (int): The decimal number to convert
        
    Returns:
        str: Binary representation with 'db' prefix and suffix
    """
    # Convert decimal to binary, removing the '0b' prefix that bin() adds
    binary = bin(decimal)[2:]
    
    # Add 'db' prefix and suffix
    result = "db" + binary + "db"
    
    return result