def Strongest_Extension(class_name, extensions):
    """
    Returns a string in the format <class_name>.<strongest_extension>
    where the strongest extension is determined by its "strength":
    - Each uppercase letter contributes +1
    - Each lowercase letter contributes -1
    - Digits, symbols, or non-alphabetic characters contribute 0

    Args:
        class_name: A string representing the class name
        extensions: A list of strings representing extension names

    Returns:
        A string in format "class_name.strongest_extension"

    Raises:
        AttributeError: If class_name is not a string
        TypeError: If extensions is not a list
        ValueError: If extensions list is empty
    """
    # Check if class_name is a string
    if not isinstance(class_name, str):
        raise AttributeError("class_name must be a string")

    # Check if extensions is a list
    if not isinstance(extensions, list):
        raise TypeError("extensions must be a list")

    # Check if extensions list is empty
    if len(extensions) == 0:
        raise ValueError("extensions list cannot be empty")

    def calculate_strength(extension):
        """Calculate the strength of an extension string"""
        strength = 0
        for char in extension:
            if char.isupper():
                strength += 1
            elif char.islower():
                strength -= 1
            # Digits, symbols, and non-alphabetic characters contribute 0
        return strength

    # Find the strongest extension
    max_strength = float('-inf')
    strongest_ext = None

    for extension in extensions:
        strength = calculate_strength(extension)
        if strength > max_strength:
            max_strength = strength
            strongest_ext = extension

    return f"{class_name}.{strongest_ext}"