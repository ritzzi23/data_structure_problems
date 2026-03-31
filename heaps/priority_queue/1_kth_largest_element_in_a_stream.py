#Brute Force
'''
Time: O(n log n) per call — sort() is called every time add is invoked, where n is the current length of self.nums
Space: O(n) — storing all elements in self.nums
'''

from typing import List
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse= True)
        return self.nums[(self.k)-1]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#--------------------------------------------------------------------------
#For kth largest, keep top k elements in a min-heap, and the heap top is the answer.
#Min Heap Approach

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        #add all the elements in the heap
        for elem in nums:
            heapq.heappush(self.heap,elem)
            #if the size of the heap is greater than k, remove the smallest element
            if (len(self.heap)>self.k):
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        #add the new element in the heap
        heapq.heappush(self.heap,val)
        #if the size of the heap is greater than k, remove the smallest element
        if (len(self.heap)>self.k):
            heapq.heappop(self.heap)
        #return the smallest element which is the kth largest element
        return self.heap[0] 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)