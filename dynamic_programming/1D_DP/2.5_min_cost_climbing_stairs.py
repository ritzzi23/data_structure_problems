# state: memo[n] means the minimum cost to reach step n
# by taking either 1 step from (n-1) paying cost[n-1]
# or 2 steps from (n-2) paying cost[n-2]

#Brute Force
#Time Complexity: O(2^n)
#Space Complexity: O(n)
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #We are using helper function because we want to iterate on indices than on cost array
        def helper(i):
            #because we can start from both index 0 and 1 
            #we do not need to pay anything for that 
            #Base condition
            if i <= 1:
                return 0
            #cost(i) = 
            # min(cost(i-1) + jump_cost_coming from i-1 location, 
            # cost(i-2) + jump_cost_coming from i-2 location)
            return (min(
                helper(i-1) + cost[i-1],
                helper(i-2) + cost[i-2]
            ))



        return helper(len(cost))

#--------------------------------------------------------
#Memoization Solution
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def helper(i):
            #because we can start from both index 0 and 1 
            #we do not need to pay anything for that 
            #Base condition
            if i <= 1:
                return 0
            #cost(i) = min(cost(i-1) + jump_cost_coming from i-1 location, cost(i-2) + jump_cost_coming from i-2 location)
            if i not in memo: #Time Complexity: O(n)
                memo[i] =  (min(
                helper(i-1) + cost[i-1],
                helper(i-2) + cost[i-2]
            ))
                        
            return memo[i]

        return helper(len(cost))
#--------------------------------------------------------
#Tabulation Solution
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #because we can start from both index 0 and 1 
        #we do not need to pay anything for that 
        #Base condition
        if n <= 1:
            return 0
        dp = [0] * (n+1)
        #State here is the total cost of coming to this stair
        dp[0], dp[1] =  0,0
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+ cost[i-1],dp[i-2]+ cost[i-2])
            #cost(i) = min(cost(i-1) + jump_cost_coming from i-1 location, cost(i-2) + jump_cost_coming from i-2 location)

        return dp[n]



