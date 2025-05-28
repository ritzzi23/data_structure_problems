from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        # code here
        n = len(adj)
        
        in_degree = [0] * n
        
        #indegree updated
        for row in range(n):
            for col in adj[row]:
                in_degree[col] += 1
        
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            
            for v in adj[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        if len(result) == n:
            return False
        else:
            return True