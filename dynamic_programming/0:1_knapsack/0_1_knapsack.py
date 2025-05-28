'''A thief wants to rob a store. 
He is carrying a bag of capacity W. 
The store has ‘n’ items. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. 
He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction. 
We need to find the maximum value of items that the thief can steal.'''


def recursive_knapsack(weight,values, size, capacity):
    #base_case
    if capacity==0 or size==0:
        return 0
    if(weight[size-1] <= capacity):
        #if include the weight
        return max(values[size-1] + recursive_knapsack(weight,values, size-1, capacity-weight[size-1]),
                   #if weight not included
                   recursive_knapsack(weight,values, size-1, capacity))
    else: #(weight[size-1] > capacity):
        #if include the weight
        return (recursive_knapsack(weight,values, size-1, capacity))
    

def top_down_knapsack(weight,values, size, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(size + 1)]
    # Initialization: if capacity is 0 or items are 0, value is 0
    for i in range(size + 1):
        dp[i][0] = 0
    for j in range(capacity + 1):
        dp[0][j] = 0

    #choice diagram

    for i in range(1, size + 1):
        for j in range(1, capacity + 1):
            #if include the weight
            if weights[i - 1] <= j:
                dp[i][j] = max(
                    values[i - 1] + dp[i - 1][j - weights[i - 1]],
                    dp[i - 1][j] #if weight included and next sums
                )
            else: #if include the weight
                dp[i][j] = dp[i - 1][j]

    return dp[size][capacity] 

    
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 7
print(top_down_knapsack(weights, values, len(weights), capacity))


