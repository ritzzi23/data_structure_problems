from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def check_cycle(node, adj, visited, parent):
            visited[node] = True
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if visited[neighbour]:
                    return 1
                if check_cycle(neighbour, adj, visited, node):
                    return 1
            return 0

        visited = [False] * len(adj)
        for i in range(len(adj)):
            if not visited[i]:
                if check_cycle(i, adj, visited, -1):
                    return 1
        return 0