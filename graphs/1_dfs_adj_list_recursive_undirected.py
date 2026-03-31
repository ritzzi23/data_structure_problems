#Perfect Code no issues
#Time Complexity: O(V + E) where V is the number of vertices and E is
#Space Complexity: O(V) for the visited array and the recursion stack in the worst case.
class Solution:
    def dfsOfGraph(self, V, adj):
      result = []
      def dfs_helper(i,adj,visited,result):
        visited[i] = True
        result.append(i)
        for neigh in adj[i]:
          if not visited[neigh]:
            dfs_helper(neigh,adj,visited,result)

      visited = [False] * len(adj)
      for i in range(len(adj)):
        if not visited[i]:
          dfs_helper(i,adj,visited,result)
      
      return result

a = Solution()
V = 4
adj = [[1, 3], [2, 0], [1], [0]]
print(a.dfsOfGraph(V, adj))