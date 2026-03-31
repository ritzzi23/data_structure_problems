#Brute Force

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_length = 0
        #This loop is for the starting point of the window  
        for i in range(len(s)): #Time Complexity: O(n)
            #We are calculating the frequency of each character in the current window
            freq = {}
            max_freq = 0
            #This loop is for the ending point of the window  
            for j in range(i,len(s)): #Time Complexity: O(n)
                #We are calculating the frequency of each character in the current window
                if s[j] not in freq:
                    freq[s[j]] = 0
                freq[s[j]] += 1

                max_freq = max(max_freq,freq[s[j]])
                #Once we have the max_freq we can calculate the replacement
                #Replacement is the number of characters that are not the most frequent character
                #Replacement = window size - max_freq
                replacement = (j-i+1) - max_freq
                #If the replacement is less than or equal to k then we can replace the characters
                if replacement <= k:
                    #We can replace the characters to make the window valid
                    #AND String with longest repeating character is the current window size
                    max_length = max(max_length,(j-i+1))
        return max_length

#----------------------------------------------------------
#Optimal Solution
#Time Complexity: O(n)
#Space Complexity: O(k)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = {}
        max_freq = 0
        max_length = 0

        for end in range(len(s)):
            if s[end] not in freq:
                freq[s[end]] = 0
            freq[s[end]] += 1

            if freq[s[end]] > max_freq:
                max_freq = freq[s[end]]

            #Replacement is the number of characters that are not the most frequent character
            #Replacement = window size - max_freq
            #If the replacement is less than or equal to k then we can replace the characters
            
            #We need to shrink the window only when the window is invalid 
            #i.e. when the replacement is greater than k
            while (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            #We check if the window size is greater than the max_length
            #and the window is valid (Replacement <= k)
            #if both are true then we update the max_length
            if (end - start + 1) > max_length:
                max_length = end - start + 1

        return max_length




#----------------------------------------------------------


#My Version of the solution
#Time Complexity: O(n)
#Space Complexity: O(k)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start= 0
        end = 0
        max_length = 0
        longest_substring = {}
        max_freq = 0
        while (end < len(s)): #Time Complexity: O(n)
            #calculation 
            if s[end] not in longest_substring:
                longest_substring[s[end]] = 0
            longest_substring[s[end]] += 1

            max_freq = max(max_freq, longest_substring[s[end]])
            max_replcaement = (end-start+1) - max_freq

            if (max_replcaement < k):
                max_length = max(max_length,(end - start +1))
                end +=1

            elif (max_replcaement == k):
                max_length = max(max_length,(end - start +1))
                end +=1

            elif (max_replcaement > k):
                while  (max_replcaement > k): #Time Complexity: O(n)
                    #Calculation
                    longest_substring[s[start]] -= 1
                    if longest_substring[s[start]] == 0:
                        del longest_substring[s[start]]

                    start += 1
                    max_replcaement = (end - start + 1) - max_freq
                max_length = max(max_length,(end - start +1))
                end += 1
        
        return max_length
