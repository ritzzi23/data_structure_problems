from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
      result = []
      visited = [False] * len(adj)
      queue = deque()
      def bfs_helper(queue,adj,visited,result):
        if not queue:
          return 
        node = queue.popleft()
        visited[node] = True
        result.append(node)
        for neigh in adj[node]:
          if not visited[neigh]:
            visited[neigh] = True
            queue.append(neigh)
        bfs_helper(queue,adj,visited,result)

      for i in range(len(adj)):
        if not visited[i]:
          queue.append(i)
          visited[i] = True
          bfs_helper(queue,adj,visited,result)
      
      return result

a = Solution()
V = 4
adj = [[1, 3], [2, 0], [1], [0]]
print(a.bfsOfGraph(V, adj))