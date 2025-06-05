#Pure Recursive Solution
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def cost(i):
            if i>=len(nums):
                return 0
            left = cost(i+1)
            right = cost(i+2) + nums[i]
            return max(left,right)
        return cost(0)
#-------------------------------------------------------------------------------------------
# Memoization Solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def cost(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            left = cost(i+1)
            right = cost(i+2) + nums[i]

            memo[i]=  max(left,right)
            return memo[i]
        return cost(0)
#-------------------------------------------------------------------------------------------
# Tabulation Solution
#time complexity: O(n)
#space complexity: O(n) for dp array
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #we are storing the state, which is the maximum amount of money that can be robbed from the first i houses
        dp = [0] * (n+1)
        #this is the base case, if there are no houses, the maximum amount of money that can be robbed is 0
        if n==0:
            return 0
        #we are storing these values as we need the i-1 and i-2 values to calculate the
        # maximum amount of money that can be robbed from the first i houses
        dp[0],dp[1] = 0,nums[0]
        #we are iterating from the second house to the last house
        for i in range(2,n+1):
            #skip means we do not rob the current house, 
            #so we take the maximum amount of money that can be robbed from the first i-1 houses
            skip = dp[i-1]
            #steal means we rob the current house,
            #so we take the maximum amount of money that can be robbed from the first i-2 houses 
            #plus the money from the current house and current house is nums[i-1] 
            #because dp is storing the maximum amount of money that can be robbed till the i-th house
            steal = dp[i-2] + nums[i-1]
            dp[i] = max(skip,steal) 
        #the maximum amount of money that can be robbed from the first n houses is stored in dp[n]
        return(dp[n])