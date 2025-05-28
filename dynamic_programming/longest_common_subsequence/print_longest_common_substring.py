def print_longest_common_substring(str1: str, str2: str) -> str:
    m = len(str1)
    n = len(str2)
    dp = [['' for _ in range(n+1)] for _ in range(m+1)]
    #max_length = float("-inf")
    longest = ''

    for i in range(1,m+1):
        for j in range(1,n+1):
            if (str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1] + str1[i-1]
                if len(dp[i][j]) > len(longest):
                    longest = dp[i][j]
#                max_length = max(max_length,dp[i][j])

            else:
                dp[i][j] = ''
    return longest


s1 = "abcjklp"
s2 = "acjkp"
print(print_longest_common_substring(s1,s2))
