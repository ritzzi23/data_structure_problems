#Pure Recursive Solution
# time complexity: O(log n)
# space complexity: O(log n) due to recursion stack
from typing import List
class Solution:
    def merge(self, left,right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
    def mergeSort(self,arr, l, r):
        if l == r:
            return [arr[l]]
        
        mid = (l + r) // 2
        left_half = self.mergeSort(arr, l, mid)
        right_half = self.mergeSort(arr, mid + 1, r)
        return self.merge(left_half, right_half)

'''sol = Solution()
arr = [4, 1, 3, 9, 7]
sorted_arr = sol.mergeSort(arr, 0, len(arr) - 1)
print(sorted_arr)'''

#---------------------------------------------------------------------------------------------
#Optimized Iterative Solution
# time complexity: O(n log n)
# space complexity: O(n) for the merged array
class Solution:
    def merge(self, arr, left, mid, right):
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
        
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
        
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)
#time complexity: O(n log n)
#it is n log n because we are dividing the array into halves and merging them back  
#space complexity: O(n) for the merged array