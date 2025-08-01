#Double Dictionary Approach
#time complexity: O(n)
#space complexity: O(1)
from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for sc,tc in zip(s,t):
            if sc in s_to_t:
                if s_to_t[sc] != tc:
                    return False
            else:
                s_to_t[sc] = tc
        for sc,tc in zip(s,t):
            if tc in t_to_s:
                if t_to_s[tc] != sc:
                    return False
            else:
                t_to_s[tc] = sc
        return True
#--------------------------------------------------------------
#Single Dictionary Approach
#time complexity: O(n)
#space complexity: O(1)
from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        mapped_chars = set()
        for sc,tc in zip(s,t):
            if sc in s_to_t:
                if s_to_t[sc] != tc:
                    return False
            else:
                if tc in mapped_chars:
                    return False
                s_to_t[sc] = tc
                mapped_chars.add(tc)
        return True
#--------------------------------------------------------------