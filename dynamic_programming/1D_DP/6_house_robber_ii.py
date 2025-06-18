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
