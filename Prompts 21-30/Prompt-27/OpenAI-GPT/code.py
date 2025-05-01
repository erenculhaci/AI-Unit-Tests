# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    length = len(word)

    for i in range(length - 2, 0, -1):  # skip first and last character
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return ""
