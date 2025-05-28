from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(u: int):
            visited[u] = True
            # Explore neighbors
            for v in range(n):
                if not visited[v] and isConnected[u][v] == 1:
                    dfs(v)

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count
