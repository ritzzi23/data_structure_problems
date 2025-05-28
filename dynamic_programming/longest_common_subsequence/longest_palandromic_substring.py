class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        s2 = (s[::-1])
        n = len(s2)

        dp = [['' for _ in range(n+1)] for _ in range(m+1)]
        longest_palindrome = ''

        for i in range(1,m+1):
            for j in range(1,n+1):
                if (s[i-1]== s2[j-1]):
                    dp[i][j] = dp[i-1][j-1] + s[i-1]
                    if dp[i][j] == dp[i][j][::-1] and len(dp[i][j]) > len(longest_palindrome):
                        longest_palindrome = dp[i][j]
                else:
                    dp[i][j] = ''
        return longest_palindrome
