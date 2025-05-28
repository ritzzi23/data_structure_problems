class Solution:
    # Function to return list containing vertices in Topological order
    def topologicalSort(self, adj):
        def dfs(i, visited, stack, adj):
            visited[i] = True
            for neighbour in adj[i]:
                if not visited[neighbour]:
                    dfs(neighbour, visited, stack, adj)
            
            stack.append(i)
        
        n = len(adj)
        visited = [False] * n
        stack = []
        
        for row in range(n):
            if not visited[row]:
                dfs(row, visited, stack, adj)
        
        return stack[::-1]