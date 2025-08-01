#find the number of rotations too
#time complexity: O(n^2) where n is the length of the string
#Space complexity: O(n)
from typing import List
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(goal)
        for i in range(n):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        return False
#--------------------------------------------------------------
#Optimized Solution
#time complexity: O(n) where n is the length of the string
#Space complexity: O(n)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        double = s+s
        n = len(s)
        for i in range(n):
            match = True
            for j in range(n):
                if double[i+j] != goal[j]:
                    match = False
                    break
            if match:
                return True
        return False

#--------------------------------------------------------------
#Space Optimized Solution
#time complexity: O(n^2) where n is the length of the string
#Space complexity: O(1)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)
        for shift in range(n):  # try all possible rotations
            match = True
            for j in range(n):
                if s[(shift + j) % n] != goal[j]:
                    match = False
                    break
            if match:
                return True
        return False
#--------------------------------------------------------------