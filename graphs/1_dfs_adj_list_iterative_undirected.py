#Iterative might face issue (always have issues with ordering of the neighbour elements)
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

#---------------------------------------------------------
#Iterative with helper function (iterative is always an issue)
#with order of visiting neighbours, so we reverse the neighbours
#Time Complexity: O(V + E)
#Space Complexity: O(V)
class Solution:
    def dfsOfGraph(self, V, adj):

        def dfs_helper(stack, visited, adj, result): #Time Complexity: O(V + E)
            if not stack:
                return 
            while stack:
                node = stack.pop()
                result.append(node)
                for neigh in reversed(adj[node]):
                    if not visited[neigh]:
                        visited[neigh] = True
                        stack.append(neigh)
                        
        stack = []
        result = []
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                dfs_helper(stack, visited, adj, result)
        return result
        
a = Solution()
V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(a.dfsOfGraph(V, adj))
