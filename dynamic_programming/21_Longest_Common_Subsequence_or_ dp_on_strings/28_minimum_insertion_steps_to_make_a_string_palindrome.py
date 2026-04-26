#Time Complexity: O(m*n)
#Space Complexity: O(m*n) for dp storage
#Use LCS concept
class Solution:
    def minInsertions(self, s: str) -> int:
        def longestCommonSubsequence(text1: str, text2: str) -> int:
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
        
        return len(s) - longestCommonSubsequence(s, s[::-1])
#-------------------------------------------------------------------------------------------
#Space Optimized Solution