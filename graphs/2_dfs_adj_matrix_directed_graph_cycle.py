from typing import List
from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        # code here
        def dfs_helper(node,visited,in_recursion,adj_list):
            visited[node] = True
            in_recursion[node] = True
            
            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    if dfs_helper(neighbour,visited,in_recursion,adj_list):
                        return True
                elif in_recursion[neighbour]:
                    return True
            in_recursion[node] = False
            return False
            
                    
            
        adj_list = defaultdict(list)
        #creating adjacency list from adjacency matrix
        for u,v in edges:
            adj_list[u].append(v)
        visited = [False] * V
        in_recursion = [False] * V
        
        
        for i in range(V):
            if not visited[i]:
                if dfs_helper(i,visited,in_recursion,adj_list):
                    return True
        return False


a = Solution()
V = 4 
edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
print(a.isCycle(V, edges))   