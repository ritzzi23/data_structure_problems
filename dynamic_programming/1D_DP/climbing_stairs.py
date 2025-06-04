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