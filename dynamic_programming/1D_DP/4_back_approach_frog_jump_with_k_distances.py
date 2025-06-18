#Pure Recusive Solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
class Solution:
    def frogJump(self, heights, k):
        def helper(i):
            if (i==0):
                return 0
            min_cost = float('inf')
            for j in range(1,min(i,k)+1):
                jump_cost = abs(heights[i] - heights[i-j])
                curr_cost = helper(i-j) + jump_cost
                min_cost = min(min_cost,curr_cost)
            return min_cost
        return helper(len(heights)-1)


#-------------------------------------------------------------------------------------------
# Memoization solution
class Solution:
    def frogJump(self, heights, k):
        memo = {}
        def helper(i):
            if (i==0):
                return 0
            min_cost = float('inf')
            if i in memo:
                return memo[i]
            for j in range(1,min(i,k)+1):
                jump_cost = abs(heights[i] - heights[i-j])
                curr_cost = helper(i-j) + jump_cost
                min_cost = min(min_cost,curr_cost)
            memo[i] = min_cost
            return memo[i]
        return helper(len(heights)-1)
#-------------------------------------------------------------------------------------------
# Tabulation solution
class Solution:
    def frogJump(self, heights, k):
        dp = [0] * (len(heights))
        for i in range(1, len(heights)):
            min_cost = float('inf')
            for j in range(1,min(i,k)+1):
                jump_cost = abs(heights[i] - heights[i-j])
                curr_cost = dp[i-j] + jump_cost
                min_cost = min(min_cost,curr_cost)
            dp[i] = min_cost
        return dp[len(heights)-1]
#-------------------------------------------------------------------------------------------
