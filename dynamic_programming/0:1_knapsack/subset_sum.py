#space: O(n*sum)
def isSubsetSumRec(arr, n, sum):
    dp = [[False] * (sum + 1) for _ in range(n+1)]
    for k in range(n+1):
        dp[k][0] = True


    for i in range(1,n+1):
        for j in range(1,sum+1):
            if(arr[i-1]<= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]


arr = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(arr)
print(isSubsetSumRec(arr, n, sum))