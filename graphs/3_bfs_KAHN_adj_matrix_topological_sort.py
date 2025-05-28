from typing import List
from collections import defaultdict, deque
class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
        
        #indegree_creation
        in_degree = [0] * V
        for u in range(V):
            for v in adj_list[u]:
                in_degree[v] += 1
        
        #queue_fill
        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        
        #topological_sorting_bfs
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbour in adj_list[node]:
                in_degree[neighbour] -= 1
                
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        return result
        
            
