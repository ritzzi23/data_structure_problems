def top_down_unbounded_knapsack(weights, values, size, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(size + 1)]
    
    # Initialization: if capacity is 0 or items are 0, value is 0
    for i in range(size + 1):
        dp[i][0] = 0
    for j in range(capacity + 1):
        dp[0][j] = 0

    # Filling the DP table
    for i in range(1, size + 1):
        for j in range(1, capacity + 1):
            # If the current item can be included
            if weights[i - 1] <= j:
                dp[i][j] = max(
                    values[i - 1] + dp[i][j - weights[i - 1]],  # Include the item (unbounded)
                    dp[i - 1][j]  # Exclude the item
                )
            else:
                dp[i][j] = dp[i - 1][j]  # Exclude the item (since it's too heavy)

    return dp[size][capacity]


    
values= [1, 1]
weights = [2, 1]
capacity = 3
print(top_down_unbounded_knapsack(weights, values, len(weights), capacity))


