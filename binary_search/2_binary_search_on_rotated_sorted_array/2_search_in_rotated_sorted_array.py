#Important
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def pivot(nums):
            start = 0
            end = len(nums) - 1
            n = len(nums)
            while (start<= end):
                if nums[start] < nums[end]:
                    return start
                mid = (start + (end-start)//2)
                nex = (mid+1)%n
                prev = (mid+n-1)%n

                if(nums[mid]<= nums[nex]) and (nums[mid]<= nums[prev]):
                    return mid
                elif (nums[start]<= nums[mid]):
                    start = mid + 1
                else:
                    end = mid -1
        def search(nums,low,high, target):
            while(low<=high): 
                mid = int(low + (high-low)//2)
                if target == nums[mid]:
                    return mid
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid + 1
            return -1
        change = pivot(nums)
        left_search = search(nums,0, change-1,target)
        if left_search != -1:
            return left_search
        # Search second half
        right_search = search(nums,change, len(nums)-1,target)
        return right_search

