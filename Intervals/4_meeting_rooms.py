
#Layman Brute Force
#Time Complexity: O(n^2)
#Space Complexity: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Assumptions: the array is not sorted, overlap is only when next_start < prev_end 
        for i in range(len(intervals)):
            for j in range(i+ 1, len(intervals)):
                #here we check if current interval ends after the next interval starts
                if intervals[i][1] > intervals[j][0]:
                    #here we check if current interval starts after the next interval ends
                    if intervals[i][0] > intervals[j][1]:
                        continue
                    #here we check if current interval starts before the next interval ends
                    elif intervals[i][0] < intervals[j][1]:
                        return False
        return True

#Good Brute Force 
#Total Time Complexity: O(n^2)
#Space Complexity: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Assumptions: the array is not sorted, overlap is only when next_start < prev_end 
        for i in range(len(intervals)): #Time Complexity: O(n)
            for j in range(i+ 1, len(intervals)): #Time Complexity: O(n)
                #if the current interval is completely before the next interval(inclusive of end and start) or completely after the next interval
                if intervals[i][1] <= intervals[j][0] or intervals[i][0] >= intervals[j][1]:
                    continue
                else:
                    return False
        return True

#Best Optimal Approach
#Total Time Complexity: O(n log n)
#Space Complexity: O(1)

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0]) #Time Complexity: O(n log n)
        for i in range(1,len(intervals)): #Time Complexity: O(n)
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True
                    
