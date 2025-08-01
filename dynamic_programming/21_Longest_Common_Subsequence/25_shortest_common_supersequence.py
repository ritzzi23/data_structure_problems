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
#Time Complexity: O(m*n)
#Space Complexity: O(m*n)
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
        def findLCS(n: int, m: int, s1: str, s2: str) -> str:        
            dp = [[""] * (m+1) for _ in range(n+1)]
            
            #fill the dp table
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + s1[i-1]
                    else:
                        exlude_s1 = dp[i-1][j]
                        exlude_s2 = dp[i][j-1]
                        dp[i][j] = max(exlude_s1,exlude_s2,key=len)
            
            return dp[n][m]
        
    
