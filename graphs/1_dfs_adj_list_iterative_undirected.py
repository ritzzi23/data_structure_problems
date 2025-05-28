class Solution:
    def dfsOfGraph(self, V, adj):
        result = []
        visited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                while stack:
                    node = stack.pop()
                    result.append(node)
                    for neighbour in adj[node]:
                        if not visited[neighbour]:
                            visited[neighbour] = True
                            stack.append(neighbour)
        
        return result
        
a = Solution()
V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(a.dfsOfGraph(V, adj))