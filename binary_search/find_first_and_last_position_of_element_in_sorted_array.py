from collections import defaultdict, deque
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first(nums: List[int], target: int)-> List[int]:
            start = 0
            end = len(nums)-1
            result = -1
            while(start <= end):
                mid = int(start + (end-start)//2)

                if target == nums[mid]:
                    result = mid
                    end = mid -1
                elif target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            return result
        
        def last(nums: List[int], target: int)-> List[int]:
            start = 0
            end = len(nums)-1
            result = -1
            while(start <= end):
                mid = int(start + (end-start)//2)

                if target == nums[mid]:
                    result = mid
                    start = mid + 1
                
                elif target < nums[mid]:
                    end = mid -1
                    
                else:
                    start  = mid + 1
            return result
        

        #first occurence
        return [first(nums,target),last(nums,target)]


        
        