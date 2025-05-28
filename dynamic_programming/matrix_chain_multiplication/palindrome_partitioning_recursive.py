from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def helper(i,j):
            if(i>=j):
                return None
            pal_strings = []
            for k in range(i,j):
                temp_pal_strings = (helper(i,k) 
                            + helper(k+1, j)
                            + (s[i-1] + s[k] + s[j]))
                
            pal_strings.append(temp_pal_strings)
        return helper(1,n-1)        

