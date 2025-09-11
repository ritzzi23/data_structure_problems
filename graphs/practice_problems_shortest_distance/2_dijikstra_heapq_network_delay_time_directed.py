#Time Complexity: O((V + E) log V) where V is the number of vertices and E is the number of edges.
#Space Complexity: O(V + E) for the adjacency list and O(V) for the distance array and heap.

from collections import defaultdict
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u,v,w in times:
            adj_list[u].append((v,w))
            #if the graph were undirected, we would add the reverse edge as well and no other changes would be needed
#            adj_list[v].append((u, w))  # 👈 add reverse edge
            

        dist = [float('inf')] * (n+1)

        dist[k] = 0

        #min-heap of (distance, node)
        heap = [(0,k)]
        
        while heap:
            d,u = heapq.heappop(heap)
            for v,w in adj_list[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(heap,(dist[v],v))
        
        
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1