from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        if len(mountain) == 1:
            return [0]
        result = []
        for i in range(len(mountain)):
            if i!= 0 and i != len(mountain)-1:
                if mountain[i]>mountain[i+1] and mountain[i]>mountain[i-1]:
                    result.append(i)
        return result 