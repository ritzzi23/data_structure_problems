from typing import List

class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        # code here
        def check_cycle(row, adj, visited, in_recursion):
            visited[row] = True
            in_recursion[row] = True
            for neighbour in adj[row]:
                if visited[neighbour] and in_recursion[neighbour]:
                    return True
                if not visited[neighbour] and check_cycle(neighbour, adj, visited, in_recursion):
                    return True
            
            in_recursion[row] = False
            return False

        n = len(adj)
        visited = [False] * n
        in_recursion = [False] * n
        
        for i in range(n):
            if not visited[i]:
                if check_cycle(i, adj, visited, in_recursion):
                    return True
        
        return False