from collections import defaultdict, deque
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def pivot_elem(nums):
            start = 0
            end = len(nums)-1

                
            while start <= end:
                if nums[start] <= nums[end]:
                    return start
                mid = start + (end-start)//2
                if ((mid > 0 and mid < len(nums)-1) 
                and nums[mid] <= nums[mid-1] 
                and nums[mid] <= nums[mid+1]):
                    return mid
                elif nums[mid] < nums[end]:
                    end = mid -1              
                else:
                    start = mid + 1
            return 0
        def binary_search(nums, target, start, end):
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        n = len(nums)
        pivot = pivot_elem(nums)

        left_search = binary_search(nums, target, 0, pivot-1)
        if left_search != -1:
            return left_search
        
        # Search second half
        right_search = binary_search(nums, target, pivot, n-1)
        return right_search