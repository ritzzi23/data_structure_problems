#Pure Recussive Solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
# This code solves the unbounded knapsack problem where you can take an item multiple times.
class Solution:
    def knapSack(self, val, wt,capacity):
        def recursive(elem_index,capacity):
            #base case
            #if no items left or capacity is 0, return 0
            if (elem_index<0) or (capacity <= 0):
                return 0
            #if current weight is greater than capacity, skip this item
            #and move to the next item
            #this is the key difference from the 0/1 knapsack problem
            if wt[elem_index] > capacity:
                return recursive(elem_index-1,capacity)
            #if we can include the current item, we can take it multiple times
            include = val[elem_index] + recursive(elem_index,capacity - wt[elem_index])
            exclude =  recursive(elem_index-1,capacity)  
            
            return max(include,exclude)
            
            
        
        return recursive(len(wt)-1,capacity)
#--------------------------------------------------------------------------------------------
# Memoization Solution
# time complexity: O(n*capacity)
# space complexity: O(n*capacity) for memoization storage
class Solution:
    def knapSack(self, val, wt,capacity):
        memo = {}
        def recursive(elem_index,capacity):

            if (elem_index<0) or (capacity <= 0):
                return 0
            # Check if the result is already computed
            # and stored in the memo dictionary
            if (elem_index,capacity) in memo:
                return memo[(elem_index,capacity)]
                
            if wt[elem_index] > capacity:
                memo[(elem_index,capacity)] = recursive(elem_index-1,capacity)
                return memo[(elem_index,capacity)]
            
            include = val[elem_index] + recursive(elem_index,capacity - wt[elem_index])
            exclude =  recursive(elem_index-1,capacity)  
            
            memo[(elem_index,capacity)] = max(include,exclude)
            return memo[(elem_index,capacity)]
            
        return recursive(len(wt)-1,capacity)
#--------------------------------------------------------------------------------------------
# Tabulation Solution
# time complexity: O(n*capacity)
# space complexity: O(n*capacity) for dp array
#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        row = len(wt)
        col = capacity
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
        #maximum value that can be obtained
        #using items from index 0 to i with knapsack capacity w
        for i in range(row+1):
            for j in range(col+1):
                if i ==0 or j == 0:
                    dp[i][j] = 0
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                if wt[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    include = val[i-1] + dp[i][j- wt[i-1]]
                    exclude = dp[i-1][j]
                    
                    dp[i][j] = max(include,exclude)
        return dp[row][col]
                