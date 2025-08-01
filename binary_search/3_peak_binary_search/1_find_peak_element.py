#brute force
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = nums[i-1] if i>0 else float('-inf')
            right = nums[i+1] if i<len(nums)-1 else float('-inf')

            if nums[i]> left and nums[i]> right:
                return i
        return -1
#-------------------------------------------------------------------------------------------
# Binary Search Solution
# time complexity: O(log n)
# space complexity: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if (nums[mid]<nums[mid+1]):
                left = mid+1
            else:
                right = mid
        return left
