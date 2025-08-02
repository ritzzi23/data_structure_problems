#Pure Recursive Solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = [float('-inf')]
        if not nums:
            return float('-inf')
        #base condition
        def recursive_solution(n):
            if n<0:
                return (1,1)
            #recursive case
            prev_max,prev_min = recursive_solution(n-1)
            #current max and min
            #current_max is saved to get the maximum product
            # but we also keep track of the minimum product because
            # a negative number multiplied by a negative number can yield a positive product
            current_max = max(nums[n],nums[n]*prev_max,nums[n]*prev_min)
            current_min = min(nums[n],nums[n]*prev_max,nums[n]*prev_min)
            max_product[0] = max(max_product[0],current_max)
            return current_max,current_min
        recursive_solution(len(nums)-1)
        return max_product[0]
#-------------------------------------------------------------------------------------------
#memoization solution
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        max_product = [float('-inf')]
        if not nums:
            return float('-inf')
        #base condition
        def recursive_solution(n):
            if n<0:
                return (1,1)
            if n in memo:
                return memo[n]
            #recursive case
            prev_max,prev_min = recursive_solution(n-1)
            current_max = max(nums[n],nums[n]*prev_max,nums[n]*prev_min)
            current_min = min(nums[n],nums[n]*prev_max,nums[n]*prev_min)
            max_product[0] = max(max_product[0],current_max)
            memo[n] = current_max,current_min
            return memo[n]
        recursive_solution(len(nums)-1)
        return max_product[0]
#-------------------------------------------------------------------------------------------
#Dynamic Programming Solution
#time complexity: O(n)
#space complexity: O(n) for dp table
#state dp[i] means that when i elements are taken from the array, the maximum product of the subarray is dp[i][0]
#and the minimum product of the subarray is dp[i][1]
#We need to keep track of both maximum and minimum products because a negative number multiplied by a negative number can yield a positive product.
#So, we need to consider both the maximum and minimum
#dp[i] = (max(nums[i],nums[i]*dp[i-1][0],nums[i]*dp[i-1][1]),min(nums[i],nums[i]*dp[i-1][0],nums[i]*dp[i-1][1]))
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return float('-inf')
        
        n = len(nums)
        dp = [(0, 0)] * (n + 1)   # dp[i] = (max_product_ending_here, min_product_ending_here)
        dp[0] = (nums[0], nums[0])
        max_product = nums[0]
        
        for i in range(1, n):
            curr_max = max(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            curr_min = min(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            dp[i] = (curr_max, curr_min)
            max_product = max(max_product, curr_max)
        
        return max_product


#-------------------------------------------------------------------------------------------
