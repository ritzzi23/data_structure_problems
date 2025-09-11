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


'''
This code detects cycles in a directed graph using DFS (Depth-First Search).

What it does:
Builds an adjacency list from the given edges
Uses DFS with recursion stack tracking to detect back edges
Maintains two arrays:
visited: tracks all visited nodes
in_recursion: tracks nodes currently in the DFS recursion stack
How cycle detection works:
If we encounter a node that's already in the current recursion stack → CYCLE FOUND
If we encounter a visited node that's NOT in recursion stack → No cycle (just a cross/forward edge)
Key insight:
A cycle exists if there's a back edge (edge to an ancestor in DFS tree)
in_recursion[neighbour] == True means we found a back edge
Example with your test case:
This creates: 0→1, 0→2, 1→2, 2→0, 2→3
Cycle detected: 0→2→0
Output: True (cycle exists)

Memorable way:

"You explore paths and keep track of your current journey - if you ever meet yourself on the same path, you've found a loop!"
'''