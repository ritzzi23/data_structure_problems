
#Time complexity: O(n)
#Space complexity: O(1)
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = float('-inf')
        i = 0
        j = len(height) - 1
        while (i<j):
            water = min(height[i],height[j]) * (j-i)
            max_water = max(max_water,water)
            #always move the pointer that is pointing to the smaller height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water

