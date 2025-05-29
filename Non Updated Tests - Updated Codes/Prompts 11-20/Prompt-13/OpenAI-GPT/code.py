# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def will_it_fly(q, w):
    # Edge case: if weight is zero, only empty list can fly
    if w == 0:
        return q == []

    is_balanced = q == q[::-1]
    is_within_weight = sum(abs(x) for x in q) <= w

    return is_balanced and is_within_weight
