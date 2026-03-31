'''
Brute Force -- O(n^3) time, O(1) space
For each number, keep checking if the next consecutive number exists by scanning the entire array. Simplest but very slow.
Sorting -- O(n log n) time, O(1) space

Sort the array, then walk through it tracking the current consecutive streak. Handle duplicates by skipping them.


HashSet -- O(n) time, O(n) space

Put all numbers in a set. For each number, only start counting a sequence if num - 1 is not in the set (meaning it's the start of a sequence). Then count forward. Best approach for interviews.
'''

"""
Brute force, O(n²)

Sorting, O(n log n)

Hash set, O(n) optimal

Hash map merging, O(n)

Union Find, near O(n), but overkill
"""

#Brute Force


#Sorting - based approach
#Time Complexity: O(n log n)
#Space Complexity: O(1)
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        long_streak = 1
        current_streak = 1

        for i in range(1,len(nums)):
            #skipping duplicates
            if nums[i] == nums[i-1]:
                continue
            #if consecutive number found
            elif nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                #updating longest streak
                long_streak = max(long_streak,current_streak)
                #resetting current streak
                current_streak = 1
        #giving max because last streak might be the longest
        return max(long_streak,current_streak)

#Hash Set - based approach
#Time Complexity: O(n)
#Space Complexity: O(n)