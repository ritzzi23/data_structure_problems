#Pure Recursive Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
#-------------------------------------------------------------------------------------------
# Memoization Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n <= 2:
                return n
            if n not in memo:
                memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)
#-------------------------------------------------------------------------------------------
# Tabulation Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        if n <= 2:
            return n
        dp[0],dp[1],dp[2] = 0,1,2
        for j in range(3,n+1):
            dp[j] = dp[j-1] + dp[j-2]

        return dp[n]
#-------------------------------------------------------------------------------------------
# Space Optimized Solution 