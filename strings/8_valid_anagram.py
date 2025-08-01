#Time Complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_d = {}
        t_d = {}
        for char in s:
            if char in s_d:
                s_d[char] += 1
            else:
                s_d[char] = 1
        for char in t:
            if char in t_d:
                t_d[char] += 1
            else:
                t_d[char] = 1 
        if s_d == t_d:
            return True
        else:
            return False
