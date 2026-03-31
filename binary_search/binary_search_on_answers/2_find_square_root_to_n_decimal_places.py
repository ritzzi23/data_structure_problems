#find_square_root_to_n_decimal_places.py

#Time Complexity: O(log n)
#Space Complexity: O(1)
def sqrt_to_n_places(n, p):
    # n: number to find square root of
    # p: precision (number of decimal places)
    if n < 0: return None
    if n < 1: low, high = n, 1
    else: low, high = 1, n
    
    mid = 0
    # Run loop 100 times for high precision
    for _ in range(100):
        mid = (low + high) / 2
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return round(mid, p)

print(sqrt_to_n_places(5, 4)) # Output: 2.2361

#--------------------------------
