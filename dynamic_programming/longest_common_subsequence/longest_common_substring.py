def lcs(str1: str, str2: str) -> int:
    m = len(str1)
    n = len(str2)
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 0
    for j in range(1,n+1):
        dp[0][j] = 0
    max_length = float("-inf")

    for i in range(1,m+1):
        for j in range(1,n+1):
            if (str1[i-1] == str2[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length,dp[i][j])
            else:
                dp[i][j] = 0
    return max_length


