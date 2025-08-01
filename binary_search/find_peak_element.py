from collections import defaultdict, deque
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums)-1
        peak_elem = -1
        if len(nums) == 1:
            return 0
        while(start <= end):
            mid = start + (end-start)//2

            if (mid<len(nums)-1 and mid>0):
                if(nums[mid] > nums[mid+1]) and (nums[mid] > nums[mid-1]):
                    return mid
                elif (nums[mid] < nums[mid+1]):
                    start = mid+1
                elif (nums[mid-1] > nums[mid]):
                    end = mid-1
            elif (mid == 0):
                if (nums[mid] > nums[mid+1]):
                    return 0
                else:
                    return 1
            elif (mid == (len(nums)-1)):
                if (nums[mid] > nums[mid-1]):
                    return len(nums)-1
                else:
                    return len(nums)-2
        return -1