def pop(arr, index):
    value = arr[index]          # store the item to return

    # shift all elements after index one position left
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]    # ← O(n) part

    del arr[-1]                 # shrink the list by 1

    return value


# Example
arr = [10, 20, 30, 40, 50]
print(pop(arr, 1))  # 20
print(arr)           # [10, 30, 40, 50]

# Time Complexity: O(n) — shifting elements after the index
# Space Complexity: O(1)
# pop(-1) is O(1) since no shifting is needed
