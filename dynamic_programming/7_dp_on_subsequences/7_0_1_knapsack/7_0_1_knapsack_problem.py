#state is What is the maximum value I can get using the 
#first i items, given a remaining capacity of capacity

#Pure Recussive Solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        #base
        def max_value(i,capacity):
            if (capacity<=0) or (i<0) :
                return 0
            # not possible to include current weight 
            if wt[i] > capacity:
                return (max_value((i-1),capacity))
            
            include = val[i] + max_value((i-1),capacity-wt[i])
            exclude = max_value((i-1),capacity)

            return max(include,exclude)
        return max_value(len(wt)-1,W)
#-------------------------------------------------------------------------------------------
# Memoization Solution
#memoization solution 
#time complexity: O(n*W)
#space complexity: O(n*W) for memoization storage
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        #base
        memo = {}
        def max_value(i,capacity):
            if (capacity<=0) or (i<0) :
                return 0
            if (i,capacity) in memo:
                return memo[(i,capacity)]
            # not possible to include current weight 
            if wt[i] > capacity:
                memo[(i,capacity)] = (max_value((i-1),capacity))
                return memo[(i,capacity)]

            include = val[i] + max_value((i-1),capacity-wt[i])
            exclude = max_value((i-1),capacity)

             
            memo[(i,capacity)] = max(include,exclude)
            return memo[(i,capacity)]
        return max_value(len(wt)-1,W)
#-------------------------------------------------------------------------------------------
# Tabulation Solution
#time complexity: O(n*W)
#space complexity: O(n*W) for dp array 
#state is What is the maximum value I can get using the 
#first i items, given a remaining capacity of capacity
# dp[i][j] = Max value using first i items with capacity j

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        #base
        #[[for cols ] for rows]
        
        dp = [[-1 for _ in range(W+1)] for _ in range(len(wt)+1)]
        
        #Initialization
        for i in range(len(wt)+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
        
        for i in range(1,len(wt)+1):
            for j in range(1,W+1):
                # not possible to include current weight 
                if wt[i - 1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    include = val[i-1] + dp[i-1][j-wt[i-1]]
                    exclude = dp[i-1][j]
                    
                    dp[i][j] = max(include,exclude)
        
        return dp[len(wt)][W]
#-------------------------------------------------------------------------------------------
# Space Optimized Solution
#time complexity: O(n*W)         
##space complexity: O(W) for dp array
class Solution:
    def isSubsetSum(self, arr, sum):
        memo = {}
        def recursive(i, capacity):
            # base cases
            if capacity == 0:
                return True
            if capacity < 0 or i < 0:
                return False

            if (i, capacity) in memo:
                return memo[(i, capacity)]
            # if current element is even greater than the capacity
            if arr[i] > capacity:
                memo[(i, capacity)] = recursive(i - 1, capacity)
                return memo[(i, capacity)]

            include = recursive(i - 1, capacity - arr[i])
            exclude = recursive(i - 1, capacity)

            memo[(i, capacity)] = include or exclude
            return memo[(i, capacity)]

        return recursive(len(arr) - 1, sum)
#-------------------------------------------------------------------------------------------
#Meet in the Middle Solution