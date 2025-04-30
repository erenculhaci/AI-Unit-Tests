def Strongest_Extension(class_name, extensions):
    def strength(ext):
        cap = sum(1 for ch in ext if ch.isupper())
        sm = sum(1 for ch in ext if ch.islower())
        return cap - sm

    strongest = max(extensions, key=lambda ext: strength(ext))
    return f"{class_name}.{strongest}"
