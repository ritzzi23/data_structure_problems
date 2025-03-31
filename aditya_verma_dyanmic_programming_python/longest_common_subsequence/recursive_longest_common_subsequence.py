class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2) 
        if  m == 0 or n == 0:
            return 0
        if (text1[m-1] == text2[n-1]):
            return 1 + self.longestCommonSubsequence(text1[:m-1], text2[:n-1])
        else:
            return max(self.longestCommonSubsequence(text1, text2[:n-1]), self.longestCommonSubsequence(text1[:m-1], text2))

