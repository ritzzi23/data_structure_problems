#Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
#Space Complexity: O(V) for the visited array and the queue in the worst case.
#Iterative BFS implementation for an undirected graph using adjacency list representation.
from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
      result = []
      visited = [False] * V
      for i in range(V):
        if not visited[i]:
          q = deque([i])
          visited[i] =True
          while q:
            node = q.popleft()
            result.append(node)
            for neighbour in adj[node]:
              if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)
      return result
      
            
      
a = Solution()
V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(a.bfsOfGraph(V, adj))