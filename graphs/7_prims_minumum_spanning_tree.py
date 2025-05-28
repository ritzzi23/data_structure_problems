from typing import List
import heapq

class Solution:
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        visited = [False] * V
        min_heap = []
        heapq.heappush(min_heap,(0,0)) #weight,node
        total_weight = 0
        
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True
            total_weight += weight

            for neighbour in adj[node]:
                if not visited[neighbour[0]]:
                    heapq.heappush(min_heap,(neighbour[1],neighbour[0]))
        return total_weight
        