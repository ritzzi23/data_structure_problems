'''
    Approach	Time	Space	Idea
Brute Force	O(n²)	O(1)	For each position, scan left and right to find max walls
Prefix/Suffix Arrays	O(n)	O(n)	Pre-compute max left & max right arrays
Two Pointers	O(n)	O(1)	Move inward from both ends
Monotonic Stack	O(n)	O(n)	Find boundaries using a stack
    ''' 


#Brute Force Approach

#Total Time Complexity: O(n^2)
#Total Space Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        total_water = 0
        

        for i in range(n): #Time Complexity: O(n)
            left_max = float("-inf")
            #finding left max as the maximum has to lie of elements in the left of current index
            for j in range(0,i+1): #Time Complexity: O(n)
                left_max = max(left_max,height[j])


            right_max = float("-inf")
            #finding left max as the maximum has to lie of elements in the left of current index
            for j in range(i,n): #Time Complexity: O(n)
                right_max = max(right_max,height[j])    

            #Snow Computation 
            total_water += (min(left_max,right_max) - height[i])

        return total_water


#Prefix/Suffix Arrays Approach

#Total Time Complexity: O(n)
#Total Space Complexity: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n #Space Complexity: O(n)
        suffix_max = [0] * n #Space Complexity: O(n)
        prefix_max[0] = height[0]
        for i in range(1,n): #Time Complexity: O(n)
            prefix_max[i] = max(prefix_max[i-1],height[i])

        suffix_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffix_max[i] = max(suffix_max[i+1],height[i])

        total_water = 0
        for i in range(n):
            total_water += min(prefix_max[i],suffix_max[i]) - height[i]
        
        return total_water

#Two Pointers Approach

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

                
#Monotonic Stack Approach


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        #taking index as it will help in both height and width of the valley
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                floor_idx = stack.pop()
                # no left wall → skip
                if not stack:
                    break
                # left wall is the container's left boundary
                left = stack[-1]
                # right wall is the container's right boundary
                right = i
                #taking min of left and right because water can only be trapped up to the shorter wall
                #subtracting floor height from min height to get the height of the water
                h = min(height[left], height[right]) - height[floor_idx]
                #subtracting 1 as we are not including the floor
                width = right - left -1
                water += h * width
            stack.append(i)
        return water                 