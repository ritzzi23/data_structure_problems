#Pure Recursive Solution
#nums = [10,9,2,5,3,7,101,18]
#Time Complexity: O(2^n)
#Space Complexity: O(n)
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def recursive_solution(index,prev):
            #Base case: if index is out of bounds, return 0
            if index >= len(nums):
                return 0
            #If the current number is greater than the previous number, we can include it in the subsequence
            if prev == -1 or nums[index] > nums[prev]:
                include = 1 + recursive_solution(index + 1, index)
                exclude = recursive_solution(index + 1, prev)
                return max(include, exclude)
            else:
                #If the current number is not greater, we skip it
                return recursive_solution(index + 1, prev)
        return recursive_solution(0,-1)
#------------------------------------------------------------------------------------------------
#Memoization Solution
#Time Complexity: O(n^2)
#Space Complexity: O(n^2) for memoization storage
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def recursive_solution(index,prev):
            #Base case: if index is out of bounds, return 0
            if index >= len(nums):
                return 0
            if (index, prev) in memo:
                return memo[(index, prev)]
            #If the current number is greater than the previous number, we can include it in the subsequence
            if prev == -1 or nums[index] > nums[prev]:
                include = 1 + recursive_solution(index + 1, index)
                exclude = recursive_solution(index + 1, prev)
                memo[(index, prev)] = max(include, exclude)
                return memo[(index, prev)]
            else:
                #If the current number is not greater, we skip it
                memo[(index, prev)] = recursive_solution(index + 1, prev)
                return memo[(index, prev)]
        return recursive_solution(0,-1)
#------------------------------------------------------------------------------------------------
#Tabulation Solution
#State: dp[i] represents the length of the longest increasing subsequence that ends with nums[i]
#Time Complexity: O(n^2)
#Space Complexity: O(n) for dp storage
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        #we traverse all the elements of nums
        for i in range(n):
            #we check all the previous elements
            for j in range(i):
                #if the current element is greater than the previous element
                #we can include it in the subsequence
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #the length of the longest increasing subsequence is the maximum value in dp
        return max(dp)

#------------------------------------------------------------------------------------------------
        