
'''
Time Complexity: O(n² log n)
Total: O(n) iterations * O(n log n) sort = O(n² log n)

Space Complexity: O(1)
Sorting is in-place, only a few variables are used

'''

from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones.pop()
        while (len(stones)>1):
            stones.sort()
            last, second_last = stones[-1], stones[-2]
            if last == second_last:
                stones.pop()
                stones.pop()
                continue
            else:
                stones.pop()
                stones.pop()
                last = last - second_last
                stones.append(last)
        return stones.pop() if stones else 0
        
#----------------------------------------------------------------------------------------
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            last = stones.pop()
            second_last = stones.pop()

            if last != second_last:
                stones.append(last - second_last)

        return stones[0] if stones else 0

#------------------------------------------------------------
#using heap
'''
Here we are simulating the max heap using min heap by storing the negative of the elements
'''

'''
Time Complexity: O(n log n)

heapify is O(n)
The while loop runs up to n-1 times, each heappop/heappush is O(log n)
Total: O(n) + O(n log n) = O(n log n)
Space Complexity: O(n)

The heap list stores all n elements
Much better than the sorting approach (O(n² log n)) 
since heap operations avoid re-sorting the entire list each iteration.
'''

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones.pop()
        heap = [-1 * x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            last = -(heapq.heappop(heap))  
            second_last = -(heapq.heappop(heap))
            if last != second_last:
                key = last - second_last
                heapq.heappush(heap, -key) 
        #sometimes all elements gets destroyed so we return -heap[0] if heap else 0
        return -heap[0] if heap else 0




