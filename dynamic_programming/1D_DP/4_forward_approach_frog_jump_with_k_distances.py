#Pure Recusive Solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
class Solution:
    def frogJump(self, heights, k):
        n = len(heights)

        def dfs(i):
            if i == n - 1:
                return 0  # already at last step
            min_cost = float('inf')
            for j in range(1, k + 1):
                if i + j < n:
                    jump_cost = abs(heights[i] - heights[i + j])
                    total_cost = dfs(i + j) + jump_cost
                    min_cost = min(min_cost, total_cost)
            return min_cost

        return dfs(0)
# #-------------------------------------------------------------------------------------------
#memoization solution = Top Down Dynamic Programming
#time complexity: O(n*k)
#space complexity: O(n) for memoization storage
class Solution:
    def frogJump(self, heights, k):
        n = len(heights)
        memo = {}
        def dfs(i):
            if i == n - 1:
                return 0  # already at last step
            if i in memo:
                return memo[i]
            min_cost = float('inf')
            for j in range(1, k + 1):
                if i + j < n:
                    total_cost = dfs(i + j) + abs(heights[i] - heights[i + j])
                    min_cost = min(min_cost, total_cost)
            memo[i] = min_cost
            return memo[i]

        return dfs(0)
# #-------------------------------------------------------------------------------------------
# Tabulation solution = Bottom Up Dynamic Programming
#The conversion from above memoization solution to tabulation is very difficult
# because we have are doing recusion on next step but here the next value does not exist