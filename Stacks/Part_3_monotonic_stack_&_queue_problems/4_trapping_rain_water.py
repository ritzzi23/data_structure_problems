'''
Approach	Time	Space	Idea
Brute Force	O(n²)	O(1)	For each position, scan left and right to find max walls
Prefix/Suffix Arrays	O(n)	O(n)	Pre-compute max left & max right arrays
Two Pointers	O(n)	O(1)	Move inward from both ends
Monotonic Stack	O(n)	O(n)	Find boundaries using a stack
'''

#Time complexity: O(n) because each element is pushed and popped from the stack at most once
#Space complexity: O(n) because of the stack

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