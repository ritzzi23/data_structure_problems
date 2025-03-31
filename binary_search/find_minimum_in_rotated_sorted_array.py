from collections import defaultdict, deque
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

            
        while start <= end:
            if nums[start] <= nums[end]:
                return nums[start]
            mid = start + (end-start)//2
            if (mid > 0 and mid < len(nums)-1) and nums[mid] <= nums[mid-1] and nums[mid] <= nums[mid+1]:
                return nums[mid]
            elif nums[mid] < nums[end]:
                end = mid -1
            else:
                start = mid + 1
        return -1
