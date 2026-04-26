#Tabulation Approach
#Time Complexity: O(m*n)
#Space Complexity: O(m*n) for dp storage

class Solution:
    def LongestRepeatingSubsequence(self, s):
        # Code here
        text1, text2 = s, s
        m, n = len(text1), len(text2)
        # Create a 2D dp array initialized to 0
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        # initialization
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0

        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Ensure we do not count the same character at the same index
                if text1[i - 1] == text2[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    exclude_text1 = dp[i - 1][j]
                    exclude_text2 = dp[i][j - 1]
                    dp[i][j] = max(exclude_text1, exclude_text2)
        return dp[m][n]