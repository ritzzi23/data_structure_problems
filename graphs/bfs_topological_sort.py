from typing import List
from collections import deque

class Solution:
    def topoSort(self, N: int, adj: List[List[int]]) -> List[int]:
        # Initialize indegree list with zeros
        indegree = [0] * N
        
        # Calculate indegree for each vertex
        for u in range(N):
            for v in adj[u]:
                indegree[v] += 1
        
        # Initialize queue with vertices having 0 indegree
        que = deque()
        for i in range(N):
            if indegree[i] == 0:
                que.append(i)
        
        # Perform topological sorting
        result = []
        while que:
            # Remove a vertex with 0 indegree
            u = que.popleft()
            result.append(u)
            
            # Reduce indegree of adjacent vertices
            for v in adj[u]:
                indegree[v] -= 1
                
                # If indegree becomes 0, add to queue
                if indegree[v] == 0:
                    que.append(v)
        
        return result