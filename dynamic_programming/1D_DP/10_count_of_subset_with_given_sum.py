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
