#Practice this problem on GFG 
'''https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1'''
#time complexity: O(V+E)
#space complexity: O(V+E)

from typing import List
from collections import deque, defaultdict

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        def topo_sort(edges, V):
            # adj_list
            adj_list = defaultdict(list)
            for u, v, w in edges:
                adj_list[u].append((v, w))
            
            # indegree
            indegree = [0] * V
            for u in range(V):
                for v, _ in adj_list[u]:
                    indegree[v] += 1
                    
            # queue_fill
            queue = deque()
            for i in range(V):
                if indegree[i] == 0:
                    queue.append(i)
            
            # topo_sort_bfs
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for neigh, _ in adj_list[node]:
                    indegree[neigh] -= 1
                    
                    if indegree[neigh] == 0:
                        queue.append(neigh)
            return result, adj_list
                             
        def relax(result, adj_list):
            final_dist = [float('inf')] * V 
            final_dist[0] = 0
            for u in result:
                for v, w in adj_list[u]:
                    if final_dist[v] > final_dist[u] + w:
                        final_dist[v] = final_dist[u] + w
            for i in range(V):
                if final_dist[i] == float('inf'):
                    final_dist[i] = -1
            return final_dist
                                 
        result, adj_list = topo_sort(edges, V)
        return relax(result, adj_list)