class Solution:
    def printlongestCommonSubsequence(self, text1: str, text2: str) -> str:
        m = len(text1)
        n = len(text2)
        dp = [['' for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (text1[i-1] == text2[j-1]):
                    dp[i][j] =  dp[i-1][j-1] + text1[i-1]
                else:
#                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        return dp[m][n]

s1 = "abcde"
s2 = "bdgek"
a = Solution()
print(a.printlongestCommonSubsequence(s1,s2))        