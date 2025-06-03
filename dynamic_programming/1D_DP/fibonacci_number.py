#Pure Recursive Solution

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return (self.fib(n-1) + self.fib(n-2))
#-------------------------------------------------------------------------------------------
# Memoization Solution
# Recusive solution + Memoization(Caching) = Top Down Dynamic Programming
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def help(n):
            if n<=1:
                return n
            if n not in memo:
                memo[n] = (help(n-1) + help(n-2))
            return memo[n]
        return help(n)
#-------------------------------------------------------------------------------------------
# Tabulation Solution
# Iterative solution + Tabulation = Bottom Up Dynamic Programming
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[0],dp[1] = 0,1
        for j in range(2,n+1):
            dp[j] = dp[j-1] + dp[j-2]
        return dp[n]
#-------------------------------------------------------------------------------------------
# Space Optimized Solution
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev2,prev1 = 0,1
        for _ in range(2,n+1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        return prev1
#-------------------------------------------------------------------------------------------
