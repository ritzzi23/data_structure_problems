from collections import defaultdict, deque
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        min_count = float('inf')
        total = 0
        while(j<n):
            total += nums[j]
            if (total < target):
                j += 1
            elif (total == target):
                min_count = min(j-i+1,min_count)
                j += 1
            elif (total > target):
                while(total >= target):
                    min_count = min(j - i + 1, min_count)
                    total -= nums[i]
                    i += 1
                j += 1
        return 0 if min_count == float('inf') else min_count