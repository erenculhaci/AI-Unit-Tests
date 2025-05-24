# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def Strongest_Extension(class_name, extensions):
    """
    Finds the strongest extension for a class based on the given strength criteria.
    
    Args:
        class_name (str): The name of the class
        extensions (list): List of extension names
        
    Returns:
        str: ClassName.StrongestExtensionName format
    """
    strongest_extension = None
    max_strength = float('-inf')
    
    for extension in extensions:
        # Count uppercase and lowercase letters
        uppercase_count = sum(1 for char in extension if char.isupper())
        lowercase_count = sum(1 for char in extension if char.islower())
        
        # Calculate strength
        strength = uppercase_count - lowercase_count
        
        # Update strongest extension if current is stronger or it's the first one
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    
    # Return the result in the specified format
    return f"{class_name}.{strongest_extension}"