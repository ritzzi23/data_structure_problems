#https://chatgpt.com/share/687707f4-e550-800c-8efd-ed59af862bf4
#Pure Recursive Solution
#time complexity: O(2^(m+n))
#space complexity: O(m+n) for recursion stack
class Solution:
    def longestCommonSubstr(self, s1, s2):
        max_length = [0]  # list to hold max_length by reference

        def recursive_solution(m, n):
            # Base case
            if m < 0 or n < 0:
                return 0

            result = 0

            if s1[m] == s2[n]:
                result = 1 + recursive_solution(m - 1, n - 1)
                max_length[0] = max(max_length[0], result)

            # explore other branches without extending the substring
            recursive_solution(m - 1, n)
            recursive_solution(m, n - 1)

            return result

        recursive_solution(len(s1) - 1, len(s2) - 1)
        return max_length[0]

#-------------------------------------------------------------------------------------------
# Memoization Solution
#time complexity: O(m * n)
#space complexity: O(m * n) for memoization storage
class Solution:
    def longestCommonSubstr(self, s1, s2):
        memo = {}
        max_length = [0]
        
        def recursive_solution(m, n):
            if m < 0 or n < 0:
                return 0
            
            if (m, n) in memo:
                return memo[(m, n)]
            
            if s1[m] == s2[n]:
                result = 1 + recursive_solution(m - 1, n - 1)
                max_length[0] = max(max_length[0], result)
            else:
                result = 0  # substring breaks
            
            # Explore other starting points
            recursive_solution(m - 1, n)
            recursive_solution(m, n - 1)

            memo[(m, n)] = result
            return result
        
        recursive_solution(len(s1) - 1, len(s2) - 1)
        return max_length[0]

#-------------------------------------------------------------------------------------------
# Tabulation Solution
#time complexity: O(m * n)
#space complexity: O(m * n) for dp storage
class Solution:
    def longestCommonSubstr(self, s1, s2):
        m, n = len(s1), len(s2)

        # Create a 2D dp array initialized to 0
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        max_length = float("-inf")
        #Initialize the dp array
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    max_length = max(max_length, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_length if max_length != float("-inf") else 0
    
#-------------------------------------------------------------------------------------------
#space optimized Tabulation Solution

class Solution:
    def longestCommonSubstr(self, s1, s2):
        m, n = len(s1), len(s2)



        
        


        