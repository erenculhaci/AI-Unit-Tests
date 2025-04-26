def move_one_ball(arr):
    if not arr:
        return True  # Empty array is considered sorted

    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:  
            count += 1
            if count > 1:
                return False  # More than one "drop" means it's impossible

    return True
