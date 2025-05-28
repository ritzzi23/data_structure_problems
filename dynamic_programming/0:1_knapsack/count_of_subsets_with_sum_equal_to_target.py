#space: O(n*sum)
def countSubsets(arr, n, target):
    dp = [[0] * (target + 1) for _ in range(n+1)]
    for k in range(n+1):
        dp[k][0] = 1


    for i in range(1,n+1):
        for j in range(1,target+1):
            if(arr[i-1]<= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]


arr = [1, 1, 1, 1]
target = 1
n = len(arr)
print(countSubsets(arr, n, target))