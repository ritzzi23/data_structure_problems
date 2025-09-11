#Time Complexity: O(2^n)
#Space Complexity: O(n^2) for recursion stack
class Solution:
    def matrixMultiplication(self, arr):
        def recursive_solution(i,j):
            #Base Case
            #state: f(i,j) = minimum cost of multiplying matrices from index i to j
            if i == j:
                return 0
            min_cost = float('inf')
            #we try all possible positions to split the product from i to j
            for k in range(i,j):
                #we calculate the cost of multiplying the two resulting matrices
                cost = recursive_solution(i,k) + recursive_solution(k+1,j) + arr[i-1] * arr[k] * arr[j]
                min_cost = min(min_cost, cost)
            return min_cost
        
        return recursive_solution(1,len(arr)-1)
#--------------------------------------------------------------------------------------------
#Memoization Solution
#Time Complexity: O(n^3)
#Space Complexity: O(n^2) for memoization storage
class Solution:
    def matrixMultiplication(self, arr):
        memo = {}
        def recursive_solution(i,j):
            #Base Case
            #state: f(i,j) = minimum cost of multiplying matrices from index i to j
            if i == j:
                return 0
            min_cost = float('inf')
            if (i,j) in memo:
                return memo[(i,j)]
            #we try all possible positions to split the product from i to j
            for k in range(i,j):
                #we calculate the cost of multiplying the two resulting matrices
                cost = recursive_solution(i,k) + recursive_solution(k+1,j) + arr[i-1] * arr[k] * arr[j]
                min_cost = min(min_cost, cost)
            memo[(i,j)] = min_cost
            return memo[(i,j)]
        
        return recursive_solution(1,len(arr)-1)
#--------------------------------------------------------------------------------------------
#Tabulation Solution
#State: dp[i][j] = minimum cost of multiplying matrices from index i to j