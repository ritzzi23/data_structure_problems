#Pure Recursive Solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = [float('-inf')]
        def recursive_solution(n):
            if n<0:
                return 0
            prev_sum = recursive_solution(n-1)
            current_sum = max(nums[n],nums[n]+prev_sum)
            max_sum[0] = max(max_sum[0],current_sum)
            return current_sum
        recursive_solution(len(nums)-1)
        return max_sum[0]
    
#-------------------------------------------------------------------------------------------
#Memoization Solution
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = [float('-inf')]
        memo = {}
        def recursive_solution(n):
            if n<0:
                return 0
            if n in memo:
                return memo[n]
            prev_sum = recursive_solution(n-1)
            current_sum = max(nums[n],nums[n]+prev_sum)
            max_sum[0] = max(max_sum[0],current_sum)
            memo[n] = current_sum
            return current_sum
        recursive_solution(len(nums)-1)
        return max_sum[0]
#-------------------------------------------------------------------------------------------
#Dynamic Programming Solution
#State: dp[i] show that when i elements are taken from the array, the maximum sum of the subarray is dp[i]
#time complexity: O(n)
#space complexity: O(n) for dp table
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)
        #initialize of dp
        dp[0] = 0

        #filling dp table 
        for i in range(1,len(nums)+1):
            dp[i] = max(nums[i-1],nums[i-1]+dp[i-1])

        return max(dp[1:])

#-------------------------------------------------------------------------------------------
#Optimized Dynamic Programming Solution
        
