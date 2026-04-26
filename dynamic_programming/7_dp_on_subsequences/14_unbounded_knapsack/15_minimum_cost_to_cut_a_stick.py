#Pure Recursive Solution
# # time complexity: O(2^n)
# # space complexity: O(n) for recursion stack
class Solution:
    def cutRod(self, price):
        #code here
        total_length = len(price)
        def recursive(i,total_length):
            if i<=0 or total_length<=0:
                return 0
            if i>total_length:
                return recursive(i-1,total_length)
            
            include = price[i-1] + recursive(i,total_length - i)
            exclude = recursive(i-1,total_length)
            
            return max(include,exclude)
        
        
        return recursive(len(price),total_length)
#--------------------------------------------------------------------------------------------
# Memoization Solution
# time complexity: O(n^2)
# space complexity: O(n^2) for memoization storage
#memoization Solution

class Solution:
    def cutRod(self, price):
        memo = {}
        #code here
        total_length = len(price)
        def recursive(i,total_length):
            if i<=0 or total_length<=0:
                return 0
            if (i,total_length) in memo:
                return memo[(i,total_length)]
                
            if i>total_length:
                memo[(i,total_length)] =  recursive(i-1,total_length)
                return memo[(i,total_length)]
            
            include = price[i-1] + recursive(i,total_length - i)
            exclude = recursive(i-1,total_length)
            
            memo[(i,total_length)] =  max(include,exclude)
            return memo[(i, total_length)] 
        
        
        return recursive(len(price),total_length)
#--------------------------------------------------------------------------------------------
# Tabulation Solution
# time complexity: O(n^2)
# space complexity: O(n^2) for dp array
#tabuation Solution

class Solution:
    def cutRod(self, price):
        row = len(price) 
        col = len(price)
        total_length = len(price) + 1
        #Maximum value that can be btained using rod lengths from 1 up to i 
        #to achieve a total rod length of total_length.
        dp = [[0 for _ in range(row+1)] for _ in range(col + 1)]
        for i in range(1,row+ 1):
            for j in range(1,col+1):
                if i > j:
                    dp[i][j] = dp[i-1][j]
                
                else:
                    include = price[i-1] + dp[i][j- i]
                    exclude = dp[i-1][j]
                    
                    
                    dp[i][j] = max(include,exclude)
        return dp[row][col]
#--------------------------------------------------------------------------------------------
# Space Optimized Tabulation Solution
# time complexity: O(n^2)
# space complexity: O(n) for dp array