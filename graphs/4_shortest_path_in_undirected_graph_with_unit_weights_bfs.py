#Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
#Space Complexity: O(V + E) for the adjacency list and O(V) for the queue and distances array.
#single source shortest path in undirected graph with unit weights using BFS
#non-negative weights

#BFS is used for the shortest path when 
#all edges have the same weight (or no weights, i.e., unweighted graph).
from collections import defaultdict, deque
from typing import List
class Solution:
    def shortestPath(self, edges, N, M):
      
      adj_list = defaultdict(list)
      # Build undirected graph
      for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

# BFS Initialization
      distances = [-1] * N
      src = 0
      distances[src] = 0

      queue = deque([src])


      while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
          if distances[neighbour] == -1:
            distances[neighbour] = distances[node] + 1
            queue.append(neighbour)
      return distances
    
        
a = Solution()
N = 9
M = 10
edges = [[0,1],[0,3],[3,4],[4,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
print(a.shortestPath(edges, N, M))        


'''Try this question
https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
'''

"""Conditions for BFS Optimality:
Unweighted graph (or all weights = 1)
Single-source shortest path (from one node to all others)
Non-negative weights (satisfied by unweighted)"""