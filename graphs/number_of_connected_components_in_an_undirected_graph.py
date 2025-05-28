from collections import deque, defaultdict
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(row):
            visited[row] = True
            q = deque([row])
            while q:
                u = q.popleft()

                for v in adj_list[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)


        count = 0
        visited = [False] * n
        for row in range(n):
            if not visited[row]:
                bfs(row)
                count += 1
        return count 