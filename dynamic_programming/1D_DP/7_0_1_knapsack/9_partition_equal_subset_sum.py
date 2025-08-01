#Pure Recursive Solution
# time complexity: O(2^n)
# space complexity: O(n) for recursion stack
# This code checks if a given list of numbers can be partitioned into two subsets with equal sum.
#To fin
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def recursive(i,capacity):
            if capacity <0 or i<0:
                return False
            if capacity == 0:
                return True
            #if current element is even greater than the capcity
            if nums[i] > capacity:
                return recursive((i-1),capacity)
            
            include = recursive((i-1),capacity - nums[i])
            exclude = recursive((i-1),capacity)
            
            return include or exclude
                
        if sum(nums)%2==0:
            return recursive(len(nums)-1,sum(nums)//2)
        else:
            return False
#-------------------------------------------------------------------------------------------
# Memoization Solution
# time complexity: O(n*sum)
# space complexity: O(n*sum) for memoization storage
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def recursive_solution(i,capacity):
            if i< 0 or capacity<0:
                return False
            if capacity == 0:
                return True
            if (i,capacity) in memo:
                return memo[(i,capacity)]
            
            if (nums[i]> capacity):
                memo[(i,capacity)] = recursive_solution(i-1,capacity)
                return memo[(i,capacity)]
            include = recursive_solution(i-1,capacity-nums[i])
            exclude = recursive_solution(i-1,capacity)

            memo[(i,capacity)] =  include or exclude
            return memo[(i,capacity)]

        if sum(nums)%2==0:
            return recursive_solution(len(nums)-1, sum(nums)//2)
        else:
            return False
#-------------------------------------------------------------------------------------------
# Tabulation Solution
#State : dp[i][j] =  when we select first i elements, can we get a sum of j
# time complexity: O(n*sum)
# space complexity: O(n*sum) for dp array
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        capacity = sum(nums)//2
        if sum(nums) % 2 != 0:
            return False
        dp = [[False for _ in range(capacity + 1)] for _ in range(n+1) ]
        #Initialization
        for i in range(n+1):
            for j in range(capacity + 1):
                if j == 0:
                    dp[i][j] = True
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                # if current element is even greater than the capacity
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    include = dp[i-1][j - nums[i-1]]
                    exclude = dp[i-1][j]
                    dp[i][j] = include or exclude
                
        # the last cell will contain the answer
        return dp[n][capacity]
#-------------------------------------------------------------------------------------------
# Space Optimized Solution
#-----------------------------------------------------------------------------------------------
#Meet in the Middle Solution
'''
Split the array into two halves:
    left = nums[:n//2]
    right = nums[n//2:]
Generate all subset sums of left and right using bitmasking.
Sort the subset sums of right.
For each sum s in the subset sums of left:
    Calculate required = target - s where target = sum(nums)//2.
    Use binary search on sorted right sums to check if required exists.
If any required is found in right sums, return True.
If no match found after checking all, return False'''


#time complexity: O(n * 2^n) for generating subset sums
#space complexity: O(n * 2^n) for storing subset sums
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        total //= 2
        #Step 1: Split the array into two halves
        left = nums[:n // 2]
        right = nums[n // 2:]

        #Step 2: Generate all subset sums of left and right
        def get_subset_sums(arr):
            n = 1 << len(nums)  # 2^len(nums)
            result = []
            for num in range(n):
                subset_sum = 0
                for j in range(len(arr)):
                    if num & (1 << j):
                        subset_sum += arr[j]
                result.append(subset_sum)
            return result
        
        left_sums = get_subset_sums(left)
        right_sums = get_subset_sums(right)
        #Step 3: Sort the subset sums of right
        right_sums.sort()

        #Step 4: Check for each sum in left if the required sum exists in right
        def binary_search(arr, target):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        #Step 5: Check if any required sum exists
        for s in left_sums:
            required = total - s
            if binary_search(right_sums, required):
                return True
        return False
#-------------------------------------------------------------------------------------------

        
        

