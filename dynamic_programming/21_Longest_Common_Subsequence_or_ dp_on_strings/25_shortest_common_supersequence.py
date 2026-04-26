#Supersequence will be both strings combined minus the longest common subsequence (LCS) of the two strings.
#The length of the shortest common supersequence can be calculated as:
#len(str1) + len(str2) - len(LCS(str1, str2))
#The shortest common supersequence can be constructed by traversing the strings and the LCS.
#Pure Recursive Solution
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def recursive_solution(m,n):

            #base case
            if m<0:
                return str2[:n+1]
            if n<0:
                return str1[:m+1]

            if str1[m] == str2[n]:
                return recursive_solution(m-1,n-1) + str1[m]
            else:
                #if not matching, we have only 2 options
                #include the last character of str1 or str2
                #and find the minimum length supersequence
                include_str1 = recursive_solution(m-1,n) + str1[m]
                include_str2 = recursive_solution(m,n-1) + str2[n]
                return min(include_str1,include_str2,key=len)

        return recursive_solution(len(str1)-1,len(str2)-1)

#------------------------------------------------------------------------------------------------
#Memoization Solution
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}
        def recursive_solution(m,n):

            #base case
            if m<0:
                return str2[:n+1]
            if n<0:
                return str1[:m+1]
            if (m,n) in memo:
                return memo[(m,n)]

            if str1[m] == str2[n]:
                memo[(m,n)] = recursive_solution(m-1,n-1) + str1[m]
                return memo[(m,n)]
            else:
                #if not matching, we have only 2 options
                #include the last character of str1 or str2
                #and find the minimum length supersequence
                include_str1 = recursive_solution(m-1,n) + str1[m]
                include_str2 = recursive_solution(m,n-1) + str2[n]
                memo[(m,n)] = min(include_str1,include_str2,key=len)
                return memo[(m,n)]

        return recursive_solution(len(str1)-1,len(str2)-1)
#------------------------------------------------------------------------------------------------
#Tabulation Solution
#Time Complexity: O(m × n × (m + n))
#Space Complexity: O(m × n × (m + n))
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [[[""] for _ in range(n+1)] for _ in range(m+1)]

        #initialize the dp table
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = str2[:j]
                elif j == 0:
                    dp[i][j] = str1[:i]
        
        #fill the dp table
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    include_str1 = dp[i-1][j] + str1[i-1]
                    include_str2 = dp[i][j-1] + str2[j-1]
                    dp[i][j] = min(include_str1,include_str2,key=len)
        
        return dp[m][n]

#------------------------------------------------------------------------------------------------
#anorther approach using LCS
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
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
        m, n = len(str1), len(str2)
        lcs_length = longestCommonSubsequence(str1, str2)
        # The length of the shortest common supersequence is the sum of the lengths of both strings
        # minus the length of the longest common subsequence
        scs_length = m + n - lcs_length
        #Write the code to construct the shortest common supersequence



