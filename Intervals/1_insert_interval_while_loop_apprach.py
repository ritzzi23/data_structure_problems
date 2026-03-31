'''
Insert + Sort + Merge

Linear Scan / 3-Phase Merge (recommended)

In-place Traversal

Binary Search + Merge

Heap + Merge
'''

'''
Brute force: Insert + Sort + Merge
Better / Optimal: Linear Scan / 3-Phase Merge
Variation: In-place Traversal
Possible but not especially useful: Binary Search + Merge
Unnecessary here: Heap + Merge
'''


'''
Simple mental model

Memory trick

Two intervals merge only when they actually meet:
current start <= new end
If current starts after new ends, they are separate.

Think of the new interval as a sponge moving through the array:

intervals before it are untouched
intervals touching it get absorbed
intervals after it remain untouched
Edge cases to keep in mind
new interval comes before all intervals
new interval comes after all intervals
new interval overlaps with none
new interval overlaps with one interval
new interval overlaps with many intervals
new interval fully covers existing intervals
existing interval fully covers the new one
'''

#Insert + Sort + Merge
#Time Complexity: O(N log N)
'''
intervals.append(newInterval): O(1) on average.
intervals.sort(): O(N log N) because there are N+1 intervals.
Merging loop: O(N) because we iterate through the sorted intervals once.
Overall: Dominated by the sort, so O(N log N).
Space Complexity: O(N)
'''

'''
We take an extra array, add elements in it in sorted manner
'''

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval) #Time Complexity: O(1)
        intervals.sort() #Time Complexity: O(N log N)
        result = [] #Space Complexity: O(N)
        for i in range(len(intervals)): #Time Complexity: O(N)
            #if the result array is empty directly append the first interval
            if not result:
                result.append(intervals[i])
            elif result[-1][1]>= intervals[i][0]:
                result[-1][0] = min(result[-1][0],intervals[i][0])
                result[-1][1] = max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])
        return result

#Linear Scan / 3-Phase Merge

'''
Assumptions:
Here we use the fact that:

intervals are already sorted
intervals are already non-overlapping

So we do not sort again.
-------------------------------
---------------------------------------------------------------------------------------------
-------------------------------

While placing it, 3 things can happen to each old interval:

it is completely before the new one, so leave it alone
it touches or overlaps the new one, so combine them
it is completely after the new one, so leave it alone for later

'''


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


#---------------------------------
#while solution

'''Interview answer

If asked which is better here:

best / cleaner: while loop 3-phase merge
also correct: for loop with inserted flag'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1. add all intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. merge all overlapping intervals into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 3. add the merged newInterval
        result.append(newInterval)

        # 4. add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result