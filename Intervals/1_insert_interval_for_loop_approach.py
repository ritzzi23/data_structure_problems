'''
start with an empty result
keep a pointer i = 0
first, add all intervals that are completely before newInterval
condition: current interval ends before newInterval starts
intervals[i][1] < newInterval[0]
second, merge all intervals that overlap with newInterval
condition: current interval starts before or at newInterval end
intervals[i][0] <= newInterval[1]
keep expanding newInterval:
start = smaller start
end = bigger end
third, append the final merged newInterval to result
fourth, add all remaining intervals after it
return result
'''

'''
Time Complexity: O(n) — Single pass through the intervals list.
Space Complexity: O(n) — The result list stores all intervals in the worst case.
'''
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        for i in range(len(intervals)):
            #the old interval is completely before the new one  
            if intervals[i][1]<newInterval[0]:
                result.append(intervals[i])
            #the old interval is completely after the new one 
            elif intervals[i][0] > newInterval[1]:
                #insert the new interval if not already inserted
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                #also insert the current interval
                result.append(intervals[i])
            else:
            #the old interval touches or overlaps the new one   
            #we update the newinterval 
                newInterval[0] = min(intervals[i][0],newInterval[0])
                newInterval[1] = max(intervals[i][1],newInterval[1])    

        #finally if after all these still the new interval is not inserted as it is the last elem of the intervals, we insert it 
        if not inserted:
            result.append(newInterval)     
        return result