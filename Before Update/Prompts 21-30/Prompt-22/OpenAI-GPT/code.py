# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def Strongest_Extension(class_name, extensions):
    def strength(ext):
        cap = sum(1 for ch in ext if ch.isupper())
        sm = sum(1 for ch in ext if ch.islower())
        return cap - sm

    strongest = max(extensions, key=lambda ext: strength(ext))
    return f"{class_name}.{strongest}"
