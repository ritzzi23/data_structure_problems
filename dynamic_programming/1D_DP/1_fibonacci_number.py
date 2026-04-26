#Brute Force Solution
#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def fib(self, n: int) -> int:
        #Base Case
        if n <= 1:
            return n
        
        #Initialisation
        prev = 0 # represents fib(i-2)
        curr = 1 # represents fib(i-1)

        #Iteration
        while n>1: #Time Complexity: O(n)
            csum = prev + curr
            prev = curr 
            curr = csum
            n-= 1
        #return curr because it is the fib(n)
        return curr

#-------------------------------------------------------------------------------------------
#Pure Recursive Solution (exponential explosion)
#Time Complexity: O(2^n)
'''
Each call to fib(n) spawns two more calls: fib(n-1) and fib(n-2).
Those each spawn two more, and so on — forming a binary recursion tree.
The tree has roughly 2^n nodes at depth n.
'''
#Space Complexity: O(n)
'''
No array or memo is used, so you might think it's O(1) — but recursion uses the call stack.
At any moment, the deepest chain of calls is fib(n) → fib(n-1) → fib(n-2) → ... → fib(0).
That's n stack frames sitting in memory simultaneously.
Once the deepest call returns, frames pop off and new ones push on — but the max depth at any point is n.
'''
class Solution:
    def fib(self, n: int) -> int:
        if n<=1: 
            return n
        return (self.fib(n-1) + self.fib(n-2)) #Time Complexity: O(2^n)
#-------------------------------------------------------------------------------------------
# Memoization Solution
# Recusive solution + Memoization(Caching) = Top Down Dynamic Programming
#Time Complexity: O(n), Space Complexity: O(n) for stack + O(n) for memo = O(n)
class Solution:
    def fib(self, n: int) -> int:
        #cache to store the results of subproblems
        memo = {}
        #we make a helper function to implement the recursion
        def help(n):
            if n<=1:
                return n
            #if the result is already in the cache, return it
            #we save the recomputation of the same subproblem
            if n not in memo:
    #Time Complexity: O(n), Space Complexity: O(n) for stack + O(n) for memo = O(n)
                memo[n] = (help(n-1) + help(n-2)) 
            return memo[n]
        return help(n)
#-------------------------------------------------------------------------------------------
'''
Identify state variables → determines table dimensions (1D, 2D, 3D...).
Set table size based on input ranges.
Initialize base cases directly in the table.
Choose iteration order such that dependencies are filled first.
Translate the recurrence from recursive calls to table lookups.
Return the table cell corresponding to the original problem.

'''
# Tabulation Solution (Bottom-Up DP)
# Iterative solution + Tabulation = Bottom Up Dynamic Programming
#Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def fib(self, n: int) -> int:
        #base case check
        if n<= 1:
            return n
        # we create a list to store the results of the n+1 iterations because we want to store all the n values
        dp = [0] * (n+1) #Space Complexity: O(n)
        #base condition is stored 
        dp[0],dp[1] = 0, 1
        #loop made to remove recursion 
        #Loop order must respect dependencies
        for j in range(2,n+1): #Time Complexity: O(n)
            # doing this to go bottoms up
            #Tabulation equivalent — replace recursive calls with table lookups:
            dp[j] = dp[j-1] + dp[j-2]
        # return the final element int the dp list 
        return dp[n]
#-------------------------------------------------------------------------------------------
'''
Three conditions for space optimization:

Fixed lookback — the recurrence only reads a constant number of previous values.
No path reconstruction — you only need the final answer, not the full history.
Predictable dependencies — you know at compile time which cells are needed, not dependent on input values.
If all three hold → optimize. If any one fails → you likely need the full table.
'''
# Space Optimized Solution
#Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev2,prev1 = 0,1
        for _ in range(2,n+1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        return prev1
#-------------------------------------------------------------------------------------------
