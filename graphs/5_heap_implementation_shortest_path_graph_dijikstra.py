#key = (distance, node) 
#position_map = {node: index_in_heap_array}
class MinHeap:
    def __init__(self):
        self.heap = []
        self.position_map = {}
    def insert(self,key):
        self.heap.append(key)
        index = len(self.heap) - 1
        self.position_map[key[1]] = index
        self._heapifyUp(index)

    def extractMin(self):
        if not self.heap:
            return (-1,-1)
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.position_map[last_val[1]] = 0
            self._heapifyDown(0)
        del self.position_map[min_val[1]]
        return min_val
    def changeKey(self, index, new_val):
        if index < 0 or index >= len(self.heap):
            return 
        old_val = self.heap[index]
        self.heap[index] = new_val
        self.position_map[new_val[1]] = index
        if new_val[0] < old_val[0]:
            self._heapifyUp(index)
        else:
            self._heapifyDown(index)
    def _heapifyUp(self, i):
        while i> 0:
            parent = (i-1)//2
            if self.heap[i][0] < self.heap[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break
    def _heapifyDown(self,i):
        n = len(self.heap)
        while i <n:
            smallest = i 
            left = 2*i + 1
            right = 2*i + 2
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def _swap(self, i, j):
        self.position_map[self.heap[i][1]] = j
        self.position_map[self.heap[j][1]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def isEmpty(self):
        return len(self.heap) == 0

    def getMin(self):
        return self.heap[0] if self.heap else (-1, -1)

    def heapSize(self):
        return len(self.heap)



class Solution:
    def dijkstra(self, V, adj, S):
        minHeap = MinHeap()
        dist = [float('inf')] * V
        dist[S] = 0

        for node in range(V):
            if node == S:
                minHeap.insert((0,node))
            else:
                minHeap.insert((float('inf'),node))
        
        while not minHeap.isEmpty():
            d, u = minHeap.extractMin()

            for v_info in adj[u]:
                v, weight = v_info[0], v_info[1]
                if v in minHeap.position_map and d + weight < dist[v]:
                    dist[v] = d + weight
                    index = minHeap.position_map[v]
                    minHeap.changeKey(index, (dist[v], v))

        return dist
            
    