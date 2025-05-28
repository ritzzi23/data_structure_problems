#Dijikstra's algorithm is a single source shortest path algorithm that works for directed and undirected graphs with non-negative weights and not affected by cycles
#It uses a priority queue or min heap to store the nodes and their distances from the source node
#It is a greedy algorithm that works by selecting the node with the smallest distance from the source node and then updating the distances of the nodes connected to it


import heapq
from typing import List
class Solution:
    def dijkstra(self, V, adj, S):
        # Min-heap priority queue
        pq = [(0,S)] #current_distance, node)
        
        #initialize all distances as infinity
        result = [float('inf')] * V
        result[S] = 0
        
        # Track processed nodes
        processed = set()

        while pq:
            d, node = heapq.heappop(pq)
            
            # Skip if node already processed
            if node in processed:
                continue
                
            processed.add(node)

            for neighbour in adj[node]:
                #adj is (Node,distance)
                adjNode = neighbour[0]
                dist = neighbour[1]

                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d + dist, adjNode))
        return result




    