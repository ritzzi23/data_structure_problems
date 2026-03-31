#Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
#Space Complexity: O(V) for the visited array and the queue in the worst case.
#Iterative BFS implementation for an undirected graph using adjacency list representation.

#Time Complexity: O(V + E)
#Space Complexity: O(V)

from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
      result = [] #Space Complexity: O(V)
      visited = [False] * V
      #to handle disconnected graph we iterate through all the vertices
      for i in range(V): #Time Complexity: O(V)
        #if the vertex is not visited then we start BFS from that vertex
        if not visited[i]:
          #initialize queue and add the first vertex
          q = deque([i])
          visited[i] =True
          #while queue is not empty
          while q: #Time Complexity: O(E)
            node = q.popleft()
            result.append(node)
            #get all the neighbours of the current node
            for neighbour in adj[node]: #Time Complexity: O(E)
              #if the neighbour is not visited then mark it as visited and add it to the queue
              if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)
      return result
      
            
      
a = Solution()
V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(a.bfsOfGraph(V, adj))