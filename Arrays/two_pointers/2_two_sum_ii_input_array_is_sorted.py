#Time complexity: O(n)
#Space complexity: O(1)
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while (left!= right):
            current_sum = numbers[left] + numbers[right]
            if target > current_sum:
                left += 1
            elif target < current_sum:
                right -= 1
            else:
                return [left+1,right+1] 
        