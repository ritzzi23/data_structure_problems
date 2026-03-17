class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest_substring = {}
        n = len(s)
        max_length = 0
        while j < n:
            if s[j] not in longest_substring:
                longest_substring[s[j]] = 0
            longest_substring[s[j]] += 1
            #compare condition with window size
            if (len(longest_substring) < (j-i+1)):
                while (len(longest_substring) < (j-i+1)):
                    longest_substring[s[i]] -= 1
                    if longest_substring[s[i]] == 0:
                        del longest_substring[s[i]] 
                    i += 1
                j += 1
            elif (len(longest_substring) == (j-i+1)):
                max_length = max(max_length,j-i+1)
                j += 1
            elif (len(longest_substring) > (j-i+1)):
                while (len(longest_substring) > (j-i+1)):
                    longest_substring[s[i]] -= 1
                    if longest_substring[s[i]] == 0:
                        del longest_substring[s[i]] 
                    i += 1
                j += 1
        return max_length



        
        