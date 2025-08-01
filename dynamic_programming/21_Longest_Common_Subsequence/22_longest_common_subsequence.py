#Pure recursive Solution
#time complexity: O(2^(m+n))
#space complexity: O(m+n) for recursion stack
from typing import List
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recursive_solution(m,n):
            # Base case: if either string is empty, return 0
            if m < 0 or n<0:
                return 0
            #if the last characters match, include it in the LCS
            if (text1[m] == text2[n]):
                return 1+ recursive_solution(m-1,n-1)
            
            #if the last characters do not match, find the maximum LCS by excluding one character from either string
            else:
                exclude_text1 = recursive_solution(m-1, n)
                exclude_text2 = recursive_solution(m, n-1)
                return max(exclude_text1, exclude_text2)
        return recursive_solution(len(text1) - 1, len(text2) - 1)      

#-------------------------------------------------------------------------------------------
# Memoization Solution
#time complexity: O(m *n)
#space complexity: O(m *n) for memoization storage
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def recursive_solution(m,n):
            # Base case: if either string is empty, return 0
            if m < 0 or n<0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]

            #if the last characters match, include it in the LCS
            if (text1[m] == text2[n]):
                memo[(m,n)] =  1+ recursive_solution(m-1,n-1)
                return memo[(m,n)]
            
            #if the last characters do not match, find the maximum LCS by excluding one character from either string
            else:
                exclude_text1 = recursive_solution(m-1, n)
                exclude_text2 = recursive_solution(m, n-1)
                memo[(m,n)] = max(exclude_text1, exclude_text2)
                return memo[(m,n)]
        return recursive_solution(len(text1) - 1, len(text2) - 1)  
    
#-------------------------------------------------------------------------------------------
# Tabulation Solution
#State : dp[i][j] = length of the longest common subsequence 
# between the first i characters of text1 and the first j characters of text2
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Create a 2D dp array initialized to 0
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        # intialization
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0

        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    exclude_text1 = dp[i - 1][j]
                    exclude_text2 = dp[i][j - 1]
                    dp[i][j] = max(exclude_text1, exclude_text2)
        return dp[m][n]
#-------------------------------------------------------------------------------------------
# Space Optimized Solution
