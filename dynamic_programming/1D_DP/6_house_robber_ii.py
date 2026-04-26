#Pure Recursive Solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursive_cost(i,end):
            if i > end:
                return 0
            steal = nums[i] + recursive_cost(i+2,end)
            skip = recursive_cost(i+1,end)
            return max(steal,skip)

        n = len(nums)
        if n ==0:
            return 0
        elif n == 1:
            return nums[0]
        excluding_last_house = recursive_cost(0,n-2)
        excluding_first_house = recursive_cost(1,n-1)

        return max(excluding_last_house,excluding_first_house)
#-------------------------------------------------------------------------------------------
# Memoization Solution
#time complexity: O(n)
#space complexity: O(n) for memoization storage



class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        def helper(num):
            n = len(num)
            memo = {}
            def pattern_helper(n):
                if n<1:
                    return 0
                if n not in memo:
                    memo[n] = max(
                        pattern_helper(n-1), #skip
                        pattern_helper(n-2) + num[n-1] #acceptance of current element
                    )
                return memo[n]
            return pattern_helper(n)
        return max(helper(nums[0:n-1]),helper(nums[1:n]))











class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursive_cost(start,end):
            memo = {}
            def dfs(i):
                if i > end:
                    return 0
                if i in memo:
                    return memo[i]
                steal = nums[i] + dfs(i+2)
                skip = dfs(i+1)
                memo[i] = max(steal,skip)
                return memo[i]
            return dfs(start)

        n = len(nums)
        if n ==0:
            return 0
        elif n == 1:
            return nums[0]
        excluding_last_house = recursive_cost(0,n-2)
        excluding_first_house = recursive_cost(1,n-1)

        return max(excluding_last_house,excluding_first_house)
#-------------------------------------------------------------------------------------------
# Tabulation Solution
#time complexity: O(n)
#space complexity: O(n) for dp array
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        def helper(num):
            n = len(num)
            dp = [0] * (n+1)
            dp[0] = 0
            for i in range(1,n+1):
                dp[i] = max(
                    dp[i-1], 
                    dp[i-2] + num[i-1]
                )
            return dp[n]
        return max(helper(nums[0:n-1]),helper(nums[1:n]))
#-------------------------------------------------------------------------------------------
# Space Optimized Solution
#time complexity: O(n)
#space complexity: O(1) for constant space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(start, end):
            prev2, prev1 = 0, 0
            for i in range(start, end+1):
                curr = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, curr
            return prev1

        return max(helper(0, n-2), helper(1, n-1))