#Time Complexity: O(n log n)
#Space Complexity: O(n)
from typing import List
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        d = sorted(d.items(), key=lambda kv:kv[1], reverse=True)
        
        result = ''
        for char, freq in d:
            result += char * freq
        return(result)
