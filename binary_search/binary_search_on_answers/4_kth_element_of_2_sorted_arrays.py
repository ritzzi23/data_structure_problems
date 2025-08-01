#Kth element of 2 sorted arrays
#Binary Search Solution
# time complexity: O(log(min(m, n)))
# space complexity: O(1)
from typing import List
class Solution:
    def kthElement(self, a, b, k):
        m, n = len(a), len(b)
        # Ensure a is the smaller array
        if m > n:
            a, b, m, n = b, a, n, m
        
        # Initialize binary search bounds
        #low is maximum of 0 and kth elemeent - second array length
        #high is minimum of kth element and first array length
        low = max(0, k - n)
        high = min(k, m)

        while low <= high:
            partitionA = (low + high) // 2
            partitionB = k - partitionA
            
            maxLeftA = float('-inf') if partitionA == 0 else a[partitionA - 1]
            minRightA = float('inf') if partitionA == m else a[partitionA]
            
            maxLeftB = float('-inf') if partitionB == 0 else b[partitionB - 1]
            minRightB = float('inf') if partitionB == n else b[partitionB]
            
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                high = partitionA - 1
            else:
                low = partitionA + 1
        
        raise ValueError("Input arrays are not sorted or k is out of bounds")