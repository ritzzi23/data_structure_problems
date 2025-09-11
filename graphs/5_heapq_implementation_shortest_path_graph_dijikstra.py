
import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        dist = [float('inf')] * V
        dist[S] = 0
        
        # min-heap of (distance, node)
        heap = [(0, S)]
        
        while heap:
            d, u = heapq.heappop(heap)
            
            # Skip if this is an outdated entry
            if d > dist[u]:
                continue
            
            for v, w in adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        
        return dist
''''
the important condition

Edge weights must be non-negative.

If there are negative weights → Dijkstra fails (you need Bellman-Ford instead).

🚦 Quick intuition

Dijkstra just needs the "shortest-so-far node" to never get improved later.

That property holds for both directed and undirected graphs, as long as weights ≥ 0.

✅ So: Dijkstra works for directed and undirected graphs, with non-negative weights.'''