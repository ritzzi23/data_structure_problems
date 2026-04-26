#Pure Recursive Solution
# time complexity: O(2^n)
# space complexity: O(n) for recursion stack
from typing import List
#pure recursive
#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code here
        def recursive(i,capacity):
            #the below condition checks if no elements is left to consider
            #then there is only one sum possible which is 0
            #if capacity is also 0 then return 1 else return 0
            #here we need to realize the i is index for the elements in the array
            if i< 0:
                return 1 if capacity == 0 else 0
            #if current element is even greater than the capcity
            if arr[i] > capacity:
                return recursive(i-1,capacity)
            
            include = recursive(i-1,capacity - arr[i])
            exclude = recursive(i-1,capacity)
            
            return include + exclude
        
        return recursive((len(arr)-1),target)	
#-------------------------------------------------------------------------------------------
# Memoization Solution
# time complexity: O(n*target)
# space complexity: O(n*target) for memoization storage	
class Solution:
    def perfectSum(self, arr, target):
        memo = {}

        def recursive(i, capacity):
            if i<0:
                return 1 if capacity == 0 else 0
                
            if (i, capacity) in memo:
                return memo[(i, capacity)]

            if arr[i] > capacity:
                memo[(i, capacity)] = recursive(i - 1, capacity)
                return memo[(i, capacity)]

            include = recursive(i - 1, capacity - arr[i])
            exclude = recursive(i - 1, capacity)

            memo[(i, capacity)] = (include + exclude)
            return memo[(i, capacity)]

        return recursive(len(arr) - 1, target)
#-------------------------------------------------------------------------------------------
# Tabulation Solution
# time complexity: O(n*target)
# space complexity: O(n*target) for dp array
class Solution:
    def perfectSum(self, arr, target):
        dp = [[0 for _ in range(target+1)] for _ in range(len(arr)+1)]
        
        for i in range(len(arr)+1):
            for j in range(target+1):
                if j == 0:
                    dp[i][j] = 1
        
        for i in range(1,len(arr)+1):
            for j in range(target+1):
                if arr[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                        
                    include = dp[i-1][j-arr[i-1]]
                    exclude = dp[i-1][j]
                    
                    dp[i][j] = (include + exclude)
                
        return dp[len(arr)][target]
#-------------------------------------------------------------------------------------------
# Space Optimized Tabulation Solution
#------------------------------------------------------------------------------------------
#Meet in the Middle Solution
class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        left = arr[:n//2]
        right = arr[n//2:]

        def get_subset_sums(arr):
            result = []
            n = len(arr)
            for mask in range(1 << n):
                subset_sum = 0
                for i in range(n):
                    if mask & (1 << i):
                        subset_sum += arr[i]
                result.append(subset_sum)
            return result

        left_sums = get_subset_sums(left)
        right_sums = get_subset_sums(right)
        right_sums.sort()
        count = 0

        def count_frequency(arr, target):
            # Find the first occurrence (lower bound)
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            first = low

            # Find the position after the last occurrence (upper bound)
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            last = low

            return last - first

        for s in left_sums:
            required = target - s
            count += count_frequency(right_sums, required)

        return count
        #Step 1: Calculate the total sum of the array
        #Step 2: Check if the total sum is odd, if so return 0
        #Step 3: Split the array into two halves
        #Step 4: Generate all subset sums of left and right
        #Step 5: Sort the subset sums of right
        #Step 6: For each sum in left, calculate the required sum and count its frequency in right
        #Step 7: Return the total count of valid pairs
#--------------------------------------------------------------------------------------------