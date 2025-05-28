
#If you have no capacity (W = 0), the maximum value is 0, no matter how many items you have.
#If you have no items (n = 0), the maximum value is 0, no matter what capacity the knapsack has.

def rod_cut_top_down(prices, n):
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    #If you have no capacity (W = 0), the maximum value is 0, no matter how many items you have.

    for i in range(n+1):
        dp[i][0] = 0

    #If you have no items (n = 0), the maximum value is 0, no matter what capacity the knapsack has.

    for j in range(n+1):
        dp[0][j] = 0

    #length[i] = i

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i <= j:
                dp[i][j] = max(prices[i-1] + dp[i][j-i],
                                dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][n]



prices = [2,5,7,8,10]
n = 5
print(rod_cut_top_down(prices, n))