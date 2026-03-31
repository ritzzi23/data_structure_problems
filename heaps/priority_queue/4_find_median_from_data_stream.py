'''data structure
partition rule
size rule
the computation'''

#Brute Force
#Time Comppexity : O(1) + O(n log n) = O(n log n)
#Space Complexity: O(n)
class MedianFinder:
    def __init__(self):
        self.arr = [] #Space Complexity: O(n)
        
    def addNum(self, num: int) -> None:
        self.arr.append(num)      #Time complexity: O(1)  

    def findMedian(self) -> float:
        self.arr.sort()           #Time complexity: O(n log n)
        n = len(self.arr)

        if n %2 == 0:
            return (self.arr[(n//2)-1] + self.arr[(n//2)]) / 2
        else:
            return self.arr[(n//2)]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#-------------------------------------

#Better Approach
#Insert every elem at its correct position
#Time Complexity: O(n) + O(1) = O(n)
#Space Complexity: O(n)

class MedianFinder:

    def __init__(self):
        self.arr = [] #Space Complexity: O(n)
        
    def addNum(self, num: int) -> None: #Time complexity: O(n)
        i = 0
        while i < len(self.arr) and self.arr[i] < num:
            i+= 1
        self.arr.insert(i,num)

    def findMedian(self) -> float: #Time complexity: O(1)
        n = len(self.arr)

        if n %2 == 0:
            return (self.arr[(n//2)-1] + self.arr[(n//2)]) / 2
        else:
            return self.arr[(n//2)]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#-------------------------------------
#Best Approach
#Total Time Complexity: O(n log n) — calling addNum n times, each O(log n)
#Total Space Complexity: O(n) — all n elements stored across the two heaps


import heapq
class MedianFinder:

    def __init__(self): #Space Complexity: O(n)
        self.left_heap = [] #max_heap (as python does not have max heap, we will store values in negative form)
        self.right_heap = [] #min_heap

    def addNum(self, num: int) -> None:  #Time complexity: O(log n)
        #we will always start filling from left heap (if only one element exists it will be in left heap (smaller elements value heap))
        if not self.left_heap:
            heapq.heappush(self.left_heap, -num)
        #if the current elem is less than the max value of left heap then will we insert the curr elem in the left heap
        elif num <= -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        #if the current elem is greater than the max value of left heap then will we insert the curr elem in the right heap    
        else:
            heapq.heappush(self.right_heap, num)
        
        #Balancing
        #if the length of left heap is greater than len of right heap + 1 (because left heap can have atmost equal or 1 more element than rifht heap)
        if len(self.left_heap) > len(self.right_heap) +1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        #We balance again if not balanced
        elif len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self) -> float: # Time Complexity: O(1)

        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()