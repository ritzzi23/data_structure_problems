#Time Complexity: O(n)
#Space Complexity: O(1)
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        #initialize the pointers and the max heights
        left = 0
        water = 0
        right = len(height) -1
        #initialize the max heights
        #we will take the first and last elements as the max heights 
        # because they are the boundaries of the array
        left_max = height[0]
        right_max = height[len(height) -1]

        while left < right:
            #we will always move the pointer that is pointing to the smaller height
            if left_max < right_max:
                #move
                left += 1
                #update
                left_max = max(left_max,height[left])
                #compute
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max,height[right])
                water += right_max - height[right]
                
        return water

                
        