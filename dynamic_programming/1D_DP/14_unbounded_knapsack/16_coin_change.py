#Pure recursive solution
# time complexity: O(2^n)
# space complexity: O(n) for recursion stack
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def recursive(elem_index,amount):
            if amount == 0:
                return 0
            if elem_index <0 or amount <0:
                return float('inf')
            if coins[elem_index] > amount:
                return recursive(elem_index-1,amount)
            
            include = 1 + recursive(elem_index,amount- coins[elem_index])
            exclude = recursive(elem_index-1,amount)

            return min(include,exclude)


        result = recursive(len(coins)-1,amount)
        return -1 if result == float('inf') else result
#-------------------------------------------------------------------------------------------
# Memoization Solution
# time complexity: O(n*amount)
# space complexity: O(n*amount) for memoization storage
#memoization solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recursive(elem_index,amount):
            if amount == 0:
                return 0
            if elem_index <0 or amount <0:
                return float('inf')
            if (elem_index,amount) in memo:
                return memo[(elem_index,amount)]

            if coins[elem_index] > amount:
                memo[(elem_index,amount)]=  recursive(elem_index-1,amount)
                return memo[(elem_index,amount)]
            
            
            include = 1 + recursive(elem_index,amount- coins[elem_index])
            exclude = recursive(elem_index-1,amount)

            memo[(elem_index,amount)] =  min(include,exclude)

            return memo[(elem_index,amount)]


        result = recursive(len(coins)-1,amount)
        return -1 if result == float('inf') else result
#-------------------------------------------------------------------------------------------
# Tabulation Solution
# time complexity: O(n*amount)
# space complexity: O(n*amount) for dp array
#tabulation solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rows = len(coins)
        cols = amount

        dp = [[float('inf') for _ in range(cols +1)] for _ in range(rows+1)]
        for i in range(rows+1):
            for j in range(cols+1):
                if j == 0:
                    dp[i][j] = 0
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if coins[i-1] > j:
                    dp[i][j]=  dp[i-1][j]
                else:
                    include = 1 + dp[i][j- coins[i-1]]
                    exclude = dp[i-1][j]

                    dp[i][j] = min(include,exclude)

        return -1 if dp[rows][cols] == float('inf') else dp[rows][cols]
#-------------------------------------------------------------------------------------------
# Space Optimized Tabulation Solution
# time complexity: O(n*amount)
# space complexity: O(amount) for dp array