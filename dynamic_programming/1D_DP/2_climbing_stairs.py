#Remember that DP (bottom up) requires extra base case check


#This is a counting problem 
#Time Complexity: O(2^n), Space Complexity: O(n)
#You look backwards - where could I have been before this step?

#Pure Recursive Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        #Base case check
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2) #Time Complexity: O(2^n)
#-------------------------------------------------------------------------------------------
#Top Down + Memoization = Top Down Dynamic Programming
# Memoization Solution
#Time Complexity: O(n), 
#Space Complexity: O(n) for stack + O(n) for memo = O(n)
# state: memo[n] means the total number of ways to reach step n 
# by taking either 1 step from (n-1) or 2 steps from (n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n <= 2:
                return n
            if n not in memo:
                memo[n] = helper(n-1) + helper(n-2) #Time Complexity: O(n)
            return memo[n]
        return helper(n)
#-------------------------------------------------------------------------------------------
# Tabulation Solution
#Time Complexity: O(n), Space Complexity: O(n)
# state: dp[i] means the total number of distinct ways to reach step i
# by taking either 1 step from (i-1) or 2 steps from (i-2)
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
#Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev = 1
        curr = 2
        while n > 2:
            csum = prev + curr
            prev = curr
            curr = csum
            n -= 1
        return curr