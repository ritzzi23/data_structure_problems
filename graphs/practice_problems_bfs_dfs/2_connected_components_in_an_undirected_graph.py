#Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
#Space Complexity: O(V) for the adjacency list and the visited list
#This is the DFS approach (Recursive) (adjacency list) (undirected graph) (converting edge list to adjacency list)
from collections import defaultdict
from typing import List
class Solution:
    # Function to return connected components of the graph
    def getComponents(self, V, edges):
        # code here
        def dfs_helper(i,visited,adj_list,result,component):
            visited[i] = True
            component.append(i)
            for neigh in adj_list[i]:
                if not visited[neigh]:
                    dfs_helper(neigh,visited,adj_list,result,component)

#       (converting edge list to adjacency list)    
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        result = []
        visited = [False] * V
        for i in range(V):
            component = []
            if not visited[i]:
                dfs_helper(i,visited,adj_list,result,component)
                result.append(component)
        return result
#--------------------------------------------------------------------------------------------