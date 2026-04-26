#Pure Recursive Solution
#Time Complexity: O(2^(n+m))
#Space Complexity: O(n+m)
def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    def recursive_solution(n,m):
        if n < 0 or m < 0:
            return ""
        
        if s1[n] == s2[m]:
            return recursive_solution(n-1,m-1) + s1[n]
        
        else:
            exclude_s1 = recursive_solution(n-1,m)
            exclude_s2 = recursive_solution(n,m-1)
            return max(exclude_s1,exclude_s2,key=len)
        
    return recursive_solution(n-1,m-1)
#---------------------------------------------------------
#Memoization Solution
def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    memo = {}
    def recursive_solution(n,m):
        if n < 0 or m < 0:
            return ""
        if (n,m) in memo:
            return memo[(n,m)]
        
        if s1[n] == s2[m]:
            memo[(n,m)] = recursive_solution(n-1,m-1) + s1[n]
            return memo[(n,m)]
        
        else:
            exclude_s1 = recursive_solution(n-1,m)
            exclude_s2 = recursive_solution(n,m-1)
            memo[(n,m)] = max(exclude_s1,exclude_s2,key=len)
            return memo[(n,m)]
        
    return recursive_solution(n-1,m-1)
#---------------------------------------------------------
#tabulation solution
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
    



