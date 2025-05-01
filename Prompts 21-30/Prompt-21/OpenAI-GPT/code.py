# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def sorted_list_sum(lst):
    even_length_words = [word for word in lst if len(word) % 2 == 0]
    return sorted(even_length_words, key=lambda w: (len(w), w))
