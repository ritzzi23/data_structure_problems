#Pure Recursive Solution
#time complexity: O(2^n)
from typing import List
#space complexity: O(n) for recursion stack
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        
        def recursive(i,capacity):
            if capacity <0 or i<0:
                return False
            if capacity == 0:
                return True
            #if current element is even greater than the capcity
            if arr[i] > capacity:
                return recursive(((i-1),capacity))
            
            include = recursive(((i-1),capacity - arr[i]))
            exclude = recursive(((i-1),capacity))
            
            return include or exclude
        
        return recursive((len(arr)-1),sum)
#-------------------------------------------------------------------------------------------
# Memoization Solution
#time complexity: O(n*sum)
#space complexity: O(n*sum) for memoization storage

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        memo = {}
        def recursive(i,j):
            #base condition
            if i<0 or j<0:
                return False
            elif j==0:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
                
            if arr[i] > j:
                memo[(i,j)] = recursive(i-1,j)
                return memo[(i,j)]
            
            include = recursive(i-1,j-arr[i])
            exclude = recursive(i-1,j)
            memo[(i,j)] = include or exclude
            return memo[(i,j)]
        
            
        return recursive(len(arr)-1,sum)
#-------------------------------------------------------------------------------------------
# Tabulation Solution   
# #time complexity: O(n*sum)
# #space complexity: O(n*sum) for dp array``     
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here
        #base
        #[[for cols ] for rows]
        
        
        dp = [[False for _ in range(sum+1)] for _ in range(len(arr)+1)]
        
        #Initialization
        for i in range(len(arr)+1):
            for j in range(sum+1):
                #if sum is 0, then we can always have an empty subset
                if j == 0:
                    dp[i][j] = True
                #if there are no elements, then we cannot have a subset with non-zero sum
                elif i == 0:
                    dp[i][j] = False
        #conditions
        for i in range(1,len(arr)+1):
            for j in range(1,sum+1):
                # not possible to include current element
                if arr[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    include = dp[i-1][j-arr[i-1]]
                    exclude = dp[i-1][j]
                    
                    dp[i][j] = include or exclude
        #the last cell will contain the answer
        return dp[len(arr)][sum]
#-------------------------------------------------------------------------------------------
#Meet in the Middle Solution        
                    
            