from typing import List
from collections import defaultdict
class Solution:
    def topoSort(self, V, edges):
        # Code here
        def dfs_helper(node,adj_list,visited,stack):
            visited[node] = True
            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    dfs_helper(neighbour,adj_list,visited,stack)
            
            stack.append(node)
                    
        adj_list = defaultdict(list)            
        for u,v in edges:
            adj_list[u].append(v)
            
        stack = []
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                dfs_helper(i,adj_list,visited,stack)
        return stack[::-1]
        
a = Solution()
V = 6 
adj = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]
print(a.topoSort(V, adj))        
