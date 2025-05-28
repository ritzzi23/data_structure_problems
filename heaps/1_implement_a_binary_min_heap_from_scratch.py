'''You must create something that behaves like a Min Heap — starting from scratch — and 
it should initially be empty (i.e., contain no elements)'''


class Solution:

    def initializeHeap(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapifyUp(len(self.heap)-1)


    def extractMin(self):
        if not self.heap:
            return -1
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._heapifyDown(0)
        return min_val
        
    def changeKey(self, index, new_val):
        if index <0 or index >= len(self.heap):
            return 
        old_val = self.heap[index]
        self.heap[index] = new_val
        if new_val < old_val:
            self._heapifyUp(index)
        else:
            self._heapifyDown(index)
    
    def _heapifyUp(self, i):
        while i > 0:
            parent = (i-1)//2
            if self.heap[i] < self.heap[parent]:
                self.heap[i] , self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent 
            else:
                break
    def _heapifyDown(self, i):
        n = len(self.heap)
        while i<n:
            smallest = i
            left = 2* i + 1
            right = 2* i + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest

            else:
                break
        

    def isEmpty(self):
        return int(len(self.heap)==0)
        

    def getMin(self):
        if self.heap:
            return self.heap[0]
        return -1
        

    def heapSize(self):
        return len(self.heap)
        