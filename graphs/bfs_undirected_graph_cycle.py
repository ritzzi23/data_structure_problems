from typing import List
from collections import deque

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def bfs(node, adj, visited):
            q = deque([(node, -1)])
            visited[node] = True
            
            while q:
                node, parent = q.popleft()
                for neighbour in adj[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        q.append((neighbour, node))
                    elif neighbour != parent:
                        return True
            return False
        
        visited = [False] * len(adj)
        for i in range(len(adj)):
            if not visited[i]:
                if bfs(i, adj, visited):
                    return 1
        return 0