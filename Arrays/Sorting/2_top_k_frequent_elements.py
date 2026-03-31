"""
Sorting -- O(n log n) time, O(n) space
Count frequencies, sort by frequency, take top k. Simplest but slowest.

Heap -- O(n log k) time, O(n) space
Count frequencies, maintain a min-heap of size k. Better than sorting when k is small relative to n.

Quickselect -- O(n) average time, O(n) space
Partition-based selection on frequency. Average O(n) but worst case O(n^2).

Bucket Sort -- O(n) time, O(n) space
Use frequency as bucket index, walk buckets from right to left. Guaranteed O(n), no worst case pitfall. Best approach for interviews.
"""

#Sorting Solution
#Time Complexity: O(n log n)
#Space Complexity: O(n)
from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict()
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        result = sorted(hash_map.items(), key = lambda hp:hp[1], reverse = True )

        return [i[0] for i in result[:k]]

#-----------------
#Heap Solution
#Time Complexity: O(n log k) where k is the number of top frequent elements
#Space Complexity: O(n)
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict()
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        heap = []
        for num, freq in hash_map.items():
            #push tuple of (frequency, number) into heap
            heapq.heappush(heap,(freq, num))
            #if heap size is greater than k, pop the smallest element
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for cnt, num in heap]  

'''nums = [1,1,1,2,2,3,3,3,3], k = 2:
Counts: {1:3, 2:2, 3:4}

Push (3,1) -- heap size 1, fine
Push (2,2) -- heap size 2, fine
Push (4,3) -- heap size 3 > k, pop smallest (2,2) -- heap back to size 2
Loop ends, heap: [(3,1), (4,3)] -- correct answer'''    

#-----------------
#Bucket Sort Solution

'''How it works

First count frequency of each number

Create buckets where index = frequency

Put each number into its frequency bucket

Traverse buckets from high frequency to low

Collect first k elements'''

#Time Complexity: O(n)
#Space Complexity: O(n)
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict()
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        buckets = [[] for i in range(len(nums)+ 1)]

        for num, cnt in hash_map.items():
            buckets[cnt].append(num)

        result = []
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result