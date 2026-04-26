# State: dp(i, j) = does s[0..i-1] match p[0..j-1]
# At each step, if p[j-1] is '*', we either skip char* (zero match) or consume one char (one+ match)

# Pure Recursive Solution
# time complexity: O(2^(m+n)) worst case due to branching
# space complexity: O(m+n) for recursion stack
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursive_solution(i, j):
            # base case: pattern exhausted
            if j == 0:
                return i == 0

            # check if current chars match
            first_match = i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

            # if current pattern char is '*', two choices
            if j >= 2 and p[j - 1] == '*':
                # zero match: skip char* pair (j-2)
                # one+ match: consume one char from s, stay on same j
                zero_match = recursive_solution(i, j - 2)
                one_plus_match = first_match and recursive_solution(i - 1, j)
                return zero_match or one_plus_match
            else:
                # simple single char match
                return first_match and recursive_solution(i - 1, j - 1)

        return recursive_solution(len(s), len(p))

# -------------------------------------------------------------------------------------------
# Memoization Solution
# time complexity: O(m * n)
# space complexity: O(m * n) for memo + O(m + n) recursion stack
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def recursive_solution(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # base case: pattern exhausted
            if j == 0:
                memo[(i, j)] = i == 0
                return memo[(i, j)]

            # check if current chars match
            first_match = i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

            # if current pattern char is '*', two choices
            if j >= 2 and p[j - 1] == '*':
                zero_match = recursive_solution(i, j - 2)
                one_plus_match = first_match and recursive_solution(i - 1, j)
                result = zero_match or one_plus_match
            else:
                result = first_match and recursive_solution(i - 1, j - 1)

            memo[(i, j)] = result
            return result

        return recursive_solution(len(s), len(p))

# -------------------------------------------------------------------------------------------
# Dynamic Programming Solution
# State: dp[i][j] = when i characters taken from s and j characters taken from p, does s[0..i-1] match p[0..j-1]
# time complexity: O(m * n)
# space complexity: O(m * n) for dp table
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        # initialize dp table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # first row: patterns like a*b*c* can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # filling dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # zero match: skip char* pair
                    zero_match = dp[i][j - 2]
                    # one+ match: consume one char, stay on same pattern
                    one_plus_match = dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                    dp[i][j] = zero_match or one_plus_match
                else:
                    # single char match
                    char_match = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                    dp[i][j] = dp[i - 1][j - 1] and char_match

        return dp[m][n]