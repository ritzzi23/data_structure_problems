#Merge Sort Approach to find the median of two sorted arrays
#time complexity: O((m + n) log(m + n))
#space complexity: O(m + n) for the merged array
from typing import List
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

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        n = len(merged)
        self.mergeSort(merged, 0, n - 1)

        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]
#---------------------------------------------------------------------------------------------
#Merge Two Sorted Arrays Approach
#time complexity: O(m + n)
#space complexity: O(m + n) for the merged array
#As both arrays are already sorted, we can only merge them without sorting.
#This approach is two pointers approach
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        merged = []
        i = j = 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < m:
            merged.append(nums1[i])
            i += 1
        
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        total = m + n
        if total % 2 == 0:
            return (merged[total // 2 - 1] + merged[total // 2]) / 2
        else:
            return merged[total // 2]
#---------------------------------------------------------------------------------------------
#time complexity: O(m + n)
#space complexity: O(1) for the merged array
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        mid = total // 2
        
        i = j = 0
        count = 0
        prev = curr = 0

        while count <= mid:
            prev = curr
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            count += 1
        
        if total % 2 == 0:
            return (prev + curr) / 2
        else:
            return curr
#---------------------------------------------------------------------------------------------
#Heap Approach
##time complexity: O((m + n) log(m + n))
#space complexity: O(m + n) for the merged array
from typing import List
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        min_heap = []
        
        for num in nums1:
            heapq.heappush(min_heap, num)
        for num in nums2:
            heapq.heappush(min_heap, num)
        
        total = len(nums1) + len(nums2)
        mid = total // 2
        prev = curr = 0
        
        for i in range(mid + 1):
            prev = curr
            curr = heapq.heappop(min_heap)
        
        if total % 2 == 0:
            return (prev + curr) / 2
        else:
            return curr
#---------------------------------------------------------------------------------------------
"""✅ Approaches You Currently Have
1️⃣ Merge Sort after Concatenation
Time: O((m + n) log (m + n))

Space: O(m + n)

Remarks: Simple but wastes the fact that arrays are sorted.

2️⃣ Two-Pointer Merge
Time: O(m + n)

Space: O(m + n)

Remarks: Utilizes sorted property, straightforward, requires full merge array in memory.

3️⃣ Two-Pointer Without Extra Array
Time: O(m + n)

Space: O(1)

Remarks: Optimized space. Traverses only until mid to find the median. Good practical approach if m+n is not very large.

4️⃣ Min Heap
Time: O((m + n) log (m + n))

Space: O(m + n)

Remarks: Inefficient for this specific problem since sorted order can be exploited better.

"""