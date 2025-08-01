#Time Complexity: O(n)
#Space Complexity: O(n)
from typing import List
class Solution:
    def buildLPS(self, s):
        # code here
        n = len(s)
        if n == 0:
            return []
        if n == 1:
            return [0]

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

        return lps    
    def search(self, pat, txt):
        # code here
        result = []
        lps = self.buildLPS(pat)
        i = 0
        j = 0
        while(i<len(txt)):
            if(txt[i]==pat[j]):
                i += 1
                j += 1
                if (j== len(pat)):
    
                    result.append(i-j)
                    j = lps[j-1]
            else:
                if( j!=0):
                    j = lps[j-1]
                else:
                    i += 1
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        