# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def move_one_ball(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    for item in arr:
        if not isinstance(item, int) or isinstance(item, bool):
            raise TypeError("All elements must be integers (not bools or other types).")

    if not arr:
        return True  

    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:  
            count += 1
            if count > 1:
                return False

    return True
