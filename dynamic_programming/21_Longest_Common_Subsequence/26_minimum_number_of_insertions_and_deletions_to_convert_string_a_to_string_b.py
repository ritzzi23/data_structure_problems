#This is General Answer for converting string A to string B
#Time Complexity: O(m*n)
#Space Complexity: O(m*n) for dp storage
#Use LCS concept

#583. Delete Operation for Two Strings
class Solution:
    def minOperations(self, s1, s2):
        def LCS(s1,s2):
            m, n = len(s1), len(s2)
            dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
            #Initialize the dp table
            for i in range(m+1):
                for j in range(n+1):
                    #if either string is empty, LCS is empty
                    if i == 0:
                        dp[i][j] = 0
                    elif j == 0:
                        dp[i][j] = 0
            #Fill the dp table
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        exclude_s1 = dp[i-1][j]
                        exclude_s2 = dp[i][j-1]
                        dp[i][j] = max(exclude_s1, exclude_s2)
            return dp[m][n]
        
        lcs_length = LCS(s1, s2)
        # Number of deletions = len(s1) - LCS
        deletions = len(s1) - lcs_length
        # Number of insertions = len(s2) - LCS
        insertions = len(s2) - lcs_length
        return deletions + insertions
#-------------------------------------------------------------------------------------------
#Space Optimized Solution