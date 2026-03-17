#Approach 1: The Counting Approach (HashMap)
#Time complexity: O(n)
#Space complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if len(s) != len(t):
                return False
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in t:
            if i not in dict or dict[i] == 0:
                return False
            dict[i] -= 1
        return True
#---------------------------------------------
#Approach 2: The Sorting Approach
#Time complexity: O(n log n)
#Space complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        