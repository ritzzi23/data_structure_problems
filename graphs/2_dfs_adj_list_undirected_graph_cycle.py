class Solution:
    def isCycle(self, V, adj):
        def dfs_helper(node, adj_list, visited, parent):
            visited[node] = True
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                
                if visited[neighbour]:
                    return True
                
                if dfs_helper(neighbour, adj_list, visited, node):
                    return True
                     
            return False

        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if dfs_helper(i, adj, visited, -1):
                    return True
        return False


a = Solution()
V = 4 
adj = [[1, 2], [0], [0, 3], [2]]
print(a.isCycle(V, adj))        