def remove(arr, target):
    # Step 1: find the target — O(n)
    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            break

    if index == -1:
        raise ValueError("not in list")

    # Step 2: shift elements left — O(n)
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    del arr[-1]  # shrink the list by 1


# Example
arr = [10, 20, 30, 40, 50]
remove(arr, 30)
print(arr)  # [10, 20, 40, 50]

# Time Complexity: O(n) + O(n) = O(n) — search + shift
# Space Complexity: O(1)
