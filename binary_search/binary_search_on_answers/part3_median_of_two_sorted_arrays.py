#app 1
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
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        # STEP 1: Always make nums1 the smaller array
        # Why? So partition2 never goes out of bounds on nums2
        # Without swap: partition2 could exceed len(nums2) and CRASH
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # STEP 2: Binary search range on nums1
        # low = 0  --> take nothing from nums1
        # high = m --> take everything from nums1
        low, high = 0, m

        # STEP 3: Total left group size
        # Even total: left and right are equal
        # Odd total: left gets one extra (the +1 handles this)
        half = (m + n + 1) // 2

        while low <= high:

            # STEP 4: Pick how many from each array
            # partition1 = our choice (binary search decides)
            # partition2 = forced (left group must have exactly 'half' elements)
            partition1 = (low + high) // 2
            partition2 = half - partition1

            # STEP 5: Grab boundary values
            # If partition is at edge (0 or end), use sentinels
            # -inf means "no element on left, so anything is bigger"
            # +inf means "no element on right, so anything is smaller"
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # STEP 6: Cross boundary check
            # Within each array, left < right is guaranteed (already sorted)
            # We only check ACROSS arrays
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # VALID PARTITION FOUND
                # max(maxLeft1, maxLeft2) = like peeking top of max heap
                # min(minRight1, minRight2) = like peeking top of min heap
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)

            elif maxLeft1 > minRight2:
                # Took too many from nums1, move left
                high = partition1 - 1

            else:
                # Took too few from nums1, move right
                low = partition1 + 1
