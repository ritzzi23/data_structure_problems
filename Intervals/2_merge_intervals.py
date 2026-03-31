#Brute Force 





#----------------------------------
#Sorting + Linear Scan

#Total Time Complexity: O(n Log n)
#Space Complexity: O(n)
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #time complexity: O(n log n)
        result = [] #space complexity: O(n)
        for i in range(len(intervals)): #time complexity: O(n)
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][0] = min(result[-1][0],intervals[i][0])
                result[-1][1] = max(result[-1][1],intervals[i][1])

        return result


#----------------------------------
#Sorting + Heap-based Merge