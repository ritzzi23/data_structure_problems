from typing import List
from collections import deque

from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        if len(edges) != n - 1:
            return False
        #make adj list 
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(i,visited,adj_list):
            q = deque([(i,-1)])
            visited[i] = True
            while q:
                node, parent = q.popleft()
                for neigh in adj_list[node]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        q.append((neigh,node))
                    elif (neigh != parent):
                        return True
            return False
        
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                if bfs(i,visited,adj_list):
                    return False

        return True
