# Longest Prefix Suffix (LPS) Array
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def getLPSLength(self, s):
        # code here
        n = len(s)
        if n <= 1:
            return 0

        lps = [0] * n
        check_pointer = 0
        current_pointer = 1

        while current_pointer < n:
            if s[current_pointer] == s[check_pointer]:
                check_pointer += 1
                lps[current_pointer] = check_pointer
                current_pointer += 1
            else:
                #If mismatch then loop to check if smaller partition matches
                if check_pointer != 0:
                    check_pointer = lps[check_pointer - 1]
                else:
                    #once checked that no smaller partition matches, move to next character
                    lps[current_pointer] = 0
                    current_pointer += 1

        return lps[n - 1]
#-------------------------------------------------------------------------
#Naive Approach
#Time Complexity: O(n^2)
#Space Complexity: O(1)
from typing import List
class Solution:
    def getLPSLength(self, s):
        # code here
        n = len(s)
        max_len = 0
        
        # Check all possible lengths from 1 to n-1
        for length in range(1, n):
            prefix = s[:length]
            suffix = s[n-length:]
            
            if prefix == suffix:
                max_len = length
        
        return max_len
#-------------------------------------------------------------------------