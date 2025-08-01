#time complexity: O(log n)
#space complexity: O(1)
#This code implements a binary search algorithm to find the index of a target value in a sorted array.
#If the target is not found, it returns -1
'''#this is also implementation of inbuilt function bisect_left'''
#which returns the index where the target should be inserted to maintain sorted order.
#bisect_left is same as leftbound
#a[:i] < x <= a[i:]
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = low + (high-low)//2

            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        return low 
#--------------------------------------------------------------------------
#bisect_right is same as rightbound
#a[:i] <= x < a[i:]
from typing import List
class Solution:
    def bisect_right(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low

        