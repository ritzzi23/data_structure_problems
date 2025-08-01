#Brute Force Solution
#time complexity: O(N*L)
#space complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]  
    
#--------------------------------------------------------------
#Binary Search Solution
'''Divide and Conquer
Recursively find the LCP of left and right halves:
'''
#time complexity: O(N*L*logL) where N is the number of strings
#space complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        




#--------------------------------------------------------------
#Trie Solution
#time complexity: O(N*L) where N is the number of strings and L is the length of the longest string
#space complexity: O(N*L)
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = Trie()
        for i in strs:
            a.insert(i)
        result = ""
        node = a.root
        while True:
            if (len(node.children)!=1 or node.is_end_of_word):
                break
            char = next(iter(node.children))
            result += char
            node = node.children[char]
        return result
#---------------------------------------------------
