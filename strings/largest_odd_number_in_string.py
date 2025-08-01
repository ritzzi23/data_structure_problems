#Pure Recursive Solution
#Time Complexity: O(2^n)
#Space Complexity: O(n) for recursion stack
from typing import List
class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_value = ['']
        def recursive_solution(n):
            if n<0:
                return 
            current_value = (num[:n+1])
            if int(current_value[-1])%2!=0:
                max_value[0] = current_value
                return
            recursive_solution(n-1)

        recursive_solution(len(num)-1)
        return max_value[0]
#-------------------------------------------------------------------------------------------
#Memoization Solution
#time complexity: O(n)
#space complexity: O(n) for memoization
class Solution:
    def largestOddNumber(self, num: str) -> str:
        memo = {}
        def recursive_solution(n):
            if n < 0:
                return ''
            if n in memo:
                return memo[n]
            if int(num[n]) % 2 != 0:
                memo[n] = num[:n+1]
                return memo[n]
            memo[n] = recursive_solution(n - 1)
            return memo[n]
        
        return recursive_solution(len(num) - 1)
#-------------------------------------------------------------------------------------------
#Dynamic Programming Solution
#Time Complexity: O(n)
#Space Complexity: O(n) for dp table
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        dp = [''] * (n + 1)
        #intialize dp
        dp[0] = ''
        #filling dp table
        for i in range(1, n + 1):
            if int(num[i - 1]) % 2 != 0:
                dp[i] = num[:i]
            else:
                dp[i] = dp[i - 1]
        return dp[n]
#-------------------------------------------------------------------------------------------
#Space Optimized Solution
#Time Complexity: O(n)
#Space Complexity: O(1)
#This solution take more time because it starts from start of the string and checks each character to the end
class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ''
        for i in range(1, len(num) + 1):
            if int(num[i - 1]) % 2 != 0:
                result = num[:i]
        return result
#-------------------------------------------------------------------------------------------
#Space Optimized Solution
#Let's write a solution that starts from the end of the string and checks each character to the start
#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ''
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                result = num[:i + 1]
                break
        return result
#-------------------------------------------------------------------------------------------
