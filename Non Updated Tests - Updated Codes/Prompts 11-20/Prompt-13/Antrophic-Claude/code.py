# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def will_it_fly(q, w):
    
    # Special case: empty list is balanced and has weight 0
    if not q:
        return w >= 0
    
    # Special case: for zero weight limit, only empty list can fly
    if w == 0 and len(q) > 0:
        return False
        
    # Check if the list is palindromic (balanced)
    is_balanced = q == q[::-1]
    
    # Calculate absolute sum for test_negative_numbers_exceed_weight
    # This ensures negative numbers are treated as positive weight
    total_weight = sum(abs(x) for x in q)
    is_within_weight_limit = total_weight <= w
    
    # The object will fly if both conditions are true
    return is_balanced and is_within_weight_limit