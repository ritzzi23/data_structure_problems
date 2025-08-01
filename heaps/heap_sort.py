class Solution:
    
    def initializeHeap(self):
        # Initialize an empty heap
        self.heap = []

    def insert(self, key):
        # Insert a new key into the heap
        self.heap.append(key)
        # Maintain the heap property by moving the new key up
        #it compares the new key with its parent and swaps them if the new key is smaller
        #it continues this process until the heap property is restored till the top of the heap
        self._heapifyUp(len(self.heap)-1)


    def extractMin(self):
        # Remove and return the minimum element (the root of the heap)
        if not self.heap:
            return -1
        min_val = self.heap[0]
        #taje the last element and put it at the root
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
        # Restore the heap property by moving the root down
            self._heapifyDown(0)
        return min_val
        
    def changeKey(self, index, new_val):
        # Change the value of a key at a given index and restore the heap property
        if index <0 or index >= len(self.heap):
            # Invalid index, do nothing
            return 
        
        old_val = self.heap[index]
        self.heap[index] = new_val
        # If the new value is smaller than the old value, move it up; otherwise, move it down
        if new_val < old_val:
            # Move the new value up to restore the heap property
            self._heapifyUp(index)
        else:
            # Move the new value down to restore the heap property
            self._heapifyDown(index)
    
    def _heapifyUp(self, i):
        # Move the element at index i up to restore the heap property
        while i > 0:
            # Find the parent index
            parent = (i-1)//2
            # If the current element is smaller than its parent, swap them
            if self.heap[i] < self.heap[parent]:
                self.heap[i] , self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent 
            else:
                break

    def _heapifyDown(self, i):
        # Move the element at index i down to restore the heap property
        n = len(self.heap)
        while i<n:
            #assume the current index is the smallest
            smallest = i
            # Find the left and right children indices
            left = 2* i + 1
            right = 2* i + 2
            # Compare the current element with its children
            #if the left child is smaller than the current element, update smallest
            #if the right child is smaller than the smallest, update smallest
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            # If the smallest is not the current element, swap and continue
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
        
    def heapSort(self, arr):
        #code here
        self.initializeHeap()
        for num in arr:
            self.insert(num)
        sorted_arr = []
        while not self.isEmpty():
            sorted_arr.append(self.extractMin())
        return sorted_arr
        
        
