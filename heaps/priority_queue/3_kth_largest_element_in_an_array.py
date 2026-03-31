'''Time Complexity: O(n + k log n)

O(n) — heapify builds the max-heap (via negation) in linear time
O(k log n) — popping k-1 elements, each pop is O(log n)
Space Complexity: O(n)

The heap list stores all n elements
Note: A more optimal approach uses a min-heap of size k, giving O(n log k) time and O(k) space.'''

import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1 * x for x in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]

#------------------------------------------------------------------------
'''
More optimal for interview: Min Heap of size k
Intuition

You do not need all elements in order.

You only need to keep track of the top k largest numbers seen so far.

So:

keep a min heap of size k
if heap grows bigger than k, remove the smallest
in the end, the heap contains the k largest elements
and the top of the min heap is the kth largest

Why?

Because among the top k largest elements, the smallest one is exactly the kth largest.'''

'''
Time Complexity: O(n log k)

Iterates through all n elements
Each heappush and heappop is O(log k) since the heap never exceeds size k

Space Complexity: O(k)

Heap holds at most k elements'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for key in nums:
            heapq.heappush(heap, key)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

#------------------------------------------------------------------------
#Partition like quicksort and search one side only → best average