

# Here we are making assumption that there won't be any duplicate if the length of 
# hashmap is equal to the length of the window size 
# Because if duplicate exists that means the length of hashmap will be smaller than the length of window size 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest_substring = {}
        max_count = 0
        while j < len(s):
            # Calculation
            #Checking if the elemets exist in hashmap or not 
            if s[j] not in longest_substring:
                longest_substring[s[j]] = 0
            #incrementing the count of the element
            longest_substring[s[j]] += 1

            #Checking if the length of hashmap is smaller than the length of window size
            #This means there is a duplicate element
            if (len(longest_substring) < (j - i + 1)):
                #Shrinking the window 
                #we keep shrinking the window until the length of hashmap is equal to the length of window size
                while len(longest_substring) < (j - i + 1):
                    longest_substring[s[i]] -= 1
                    if longest_substring[s[i]] == 0:
                        del longest_substring[s[i]]
                    i += 1
                j += 1
            #Checking if the length of hashmap is equal to the length of window size
            #This means there is no duplicate element
            #Update the max_count
            elif (len(longest_substring) == (j - i + 1)):
                max_count = max(max_count,(j - i + 1))
                j += 1
            #never going to happen
#            elif (len(longest_substring) > k):
        return max_count
            
        
#--------------------------
#Standard Solutions

#Approach 2: Sliding Window with Set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

            
        
#--------------------------
#Standard Solutions