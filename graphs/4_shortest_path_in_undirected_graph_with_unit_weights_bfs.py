from collections import defaultdict, deque
from typing import List
class Solution:
    def shortestPath(self, edges, N, M):
      
      adj_list = defaultdict(list)
      for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

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
