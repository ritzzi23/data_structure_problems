#User function Template for python3
#Longest Substring with At Most K Distinct Characters
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        longest_substring = {}
        i = 0
        j = 0
        n = len(s)
        max_length = -1
        while j < n:
            if s[j] not in longest_substring:
                longest_substring[s[j]] = 0
            longest_substring[s[j]] += 1
            if(len(longest_substring) < k):
                j += 1
            elif(len(longest_substring) == k):
                max_length = max(max_length, j-i+1)
                j += 1
            elif(len(longest_substring) > k):
                while(len(longest_substring) > k):
                    longest_substring[s[i]] -= 1
                    if longest_substring[s[i]] == 0:
                        del longest_substring[s[i]]
                    i += 1
        return max_length