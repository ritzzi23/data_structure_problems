#Pure recursive solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
class Solution:
    def frogJump(self, heights):
        def cost(i):
            if i == 0:
                return 0
#to calculate the cost of jumping to the first stone, we have only cost of no jump
#therefore, we don't have cost for how the cost would be if it took 2 jumps to reach the first stone
#that's why we return the absolute value without recursion
            if i == 1:
                return abs(heights[1] - heights[0])
            return min(cost(i-1) + abs(heights[i] - heights[i-1]),
                       cost(i-2) + abs(heights[i] - heights[i-2]))
        return cost(len(heights) - 1)
#-------------------------------------------------------------------------------------------
# Memoization solution
#time complexity: O(n)
#space complexity: O(n) for memoization storage
class Solution:
    def frogJump(self, heights):
        memo = {}
        
        def cost(i):
            if i == 0:
                return 0
            if i == 1:
                return abs(heights[1] - heights[0])
            if i in memo:
                return memo[i]
            
            memo[i] = min(cost(i-1) + abs(heights[i] - heights[i-1]),
                          cost(i-2) + abs(heights[i] - heights[i-2]))
            return memo[i]
        
        return cost(len(heights) - 1)
#-------------------------------------------------------------------------------------------
# Tabulation solution
#time complexity: O(n)
#space complexity: O(n) for dp array
#User function Template for python3
class Solution:
    def minCost(self, height):
        # code here
        def cost(i):
            dp = [0] * (i+ 1)
            if i== 0:
                return 0
            elif i == 1:
                return abs(height[1] - height[0])
            dp[0],dp[1] = 0,abs(height[1] - height[0])
            for j in range(2,i+1):
                left = dp[j-1] + abs(height[j] - height[j-1])
                right = dp[j-2] + abs(height[j] - height[j-2]) 
                dp[j] = min(left,right)
            return dp[i]
        n = len(height)
        return cost(n-1)
#------------------------------------------------------------------------------------------- 
# Space Optimized solution
#time complexity: O(n)
#space complexity: O(1) for constant space
#User function Template for python3
class Solution:
    def minCost(self, height):
        # code here
        def cost(i):
            dp = [0] * (i+ 1)
            if i== 0:
                return 0
            elif i == 1:
                return abs(height[1] - height[0])
            prev2,prev1 = 0,abs(height[1] - height[0])
            for j in range(2,i+1):
                left = prev1 + abs(height[j] - height[j-1])
                right = prev2 + abs(height[j] - height[j-2]) 
                current = min(left,right)
                prev1, prev2 = current, prev1
            return prev1
        n = len(height)
        return cost(n-1)
#-------------------------------------------------------------------------------------------