#time complexity: O(log n)
#Space complexity: O(1)
from typing import List
class Solution:
    def countFreq(self, nums, target):
        def binary_search(nums, target,first):
            low = 0
            high = len(nums) -1
            result = -1
            while(low<=high): 
                mid = int(low + (high-low)//2)
                if target == nums[mid]:
                    result = mid
                    if first:
                        high = mid-1
                    else:
                        low = mid + 1
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid + 1
            return result
        first = binary_search(nums, target,True)
        if first == -1:
            return 0
        last = binary_search(nums, target, False)
        return (last-first+1)
