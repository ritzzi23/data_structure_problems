#time complexity: O(V + E)
#space complexity: O(V)
from typing import List
from collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        in_recursion = [False] * n
        safe = [False] * n

        def dfs(node):
            visited[node] = True
            in_recursion[node] = True
            
            # Check all neighbors
            for neighbor in graph[node]:
                # If neighbor is not visited, explore it
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True  # Cycle detected
                # If neighbor is in current recursion stack, cycle exists
                elif in_recursion[neighbor]:
                    return True
            
            # No cycle found through this node, mark it safe
            in_recursion[node] = False
            safe[node] = True
            return False

        # Run DFS for each unvisited node
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        # Collect all safe nodes
        
        result = []
        for i in range(n):
            if safe[i]:
                result.append(i)
        return result