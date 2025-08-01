#time complexity: O(log n)
#space complexity: O(1)
#the minimum element in a rotated sorted array is also the pivot point 
# where the array was rotated.
#and it index is the equivalent to the number of rotations.
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        n = len(nums)
        while (start<= end):
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + (end-start)//2)
            # Handle the case where mid is at the end or start of the array
            nex = (mid+1) % n
            prev = (mid+n-1) % n
            # equal to condition is important to handle duplicates
            if(nums[mid]<= nums[nex]) and (nums[mid]<= nums[prev]):
                return nums[mid]
            elif (nums[start]<= nums[mid]):
                start = mid + 1
            else:
                end = mid -1
