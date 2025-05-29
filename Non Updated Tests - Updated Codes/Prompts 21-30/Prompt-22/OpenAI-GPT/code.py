# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def Strongest_Extension(class_name, extensions):
    if not isinstance(class_name, str):
        raise AttributeError("Class name must be a string.")
    if not isinstance(extensions, list):
        raise TypeError("Extensions must be provided as a list.")
    if not extensions:
        raise ValueError("Extensions list cannot be empty.")

    def strength(ext):
        return sum(1 if c.isupper() else -1 if c.islower() else 0 for c in ext)

    strongest = extensions[0]
    max_strength = strength(strongest)

    for ext in extensions[1:]:
        current_strength = strength(ext)
        if current_strength > max_strength:
            strongest = ext
            max_strength = current_strength

    return f"{class_name}.{strongest}"
