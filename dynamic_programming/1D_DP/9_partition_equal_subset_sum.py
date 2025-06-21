#Pure Recursive Solution
# time complexity: O(2^n)
# space complexity: O(n) for recursion stack
# This code checks if a given list of numbers can be partitioned into two subsets with equal sum.
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def recursive(i,capacity):
            if capacity <0 or i<0:
                return False
            if capacity == 0:
                return True
            #if current element is even greater than the capcity
            if nums[i] > capacity:
                return recursive((i-1),capacity)
            
            include = recursive((i-1),capacity - nums[i])
            exclude = recursive((i-1),capacity)
            
            return include or exclude
                
        if sum(nums)%2==0:
            return recursive(len(nums)-1,sum(nums)//2)
        else:
            return False
#-------------------------------------------------------------------------------------------
# Memoization Solution