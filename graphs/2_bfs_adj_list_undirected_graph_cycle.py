#Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
#Space Complexity: O(V) for the visited array and the queue in the worst case.
from collections import deque

class Solution:

    def isCycle(self, V, adj):

        def bfs_helper(queue, adj_list, visited):
            while queue:
                (node, parent) = queue.popleft()
                for neighbour in adj_list[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        queue.append((neighbour, node))
                    elif neighbour != parent:
                        return True
            return False

        visited = [False] * V
        queue = deque()
        for i in range(V):
            if not visited[i]:
                queue.append((i, -1))
                visited[i] = True
                if bfs_helper(queue, adj, visited):
                    return True
        return False


a = Solution()
V = 4 
adj= [[1, 2], [0], [0, 3], [2]]
print(a.isCycle(V, adj))        

#---------------------------------------------------------
#edges conversion to adjacency list

from collections import deque, defaultdict

class Solution:
    def isCycle(self, V, edges):
        # Code here
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def bfs_helper(queue, adj_list, visited):
            while queue:
                (node, parent) = queue.popleft()
                for neigh in adj_list[node]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        queue.append((neigh, node))
                    elif neigh != parent:
                        return True
            return False
        
        visited = [False] * V
        queue = deque()
        
        for i in range(V):
            if not visited[i]:
                queue.append((i, -1))
                visited[i] = True
                if bfs_helper(queue, adj_list, visited):
                    return True
        return False