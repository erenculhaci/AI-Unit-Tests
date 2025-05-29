# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def get_closest_vowel(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    vowels = set("aeiouAEIOU")
    closest = ""

    for i in range(1, len(word) - 1):
        if word[i] in vowels:
            if word[i - 1] not in vowels and word[i + 1] not in vowels:
                closest = word[i]  # Keep updating to get rightmost

    return closest
