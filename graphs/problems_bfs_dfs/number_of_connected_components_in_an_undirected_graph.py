from collections import defaultdict, deque
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n
        count = 0
        queue = deque()
        for i in range(n):
            if not visited[i]:
                queue.append(i)
                while queue:
                    node = queue.popleft()
                    visited[node] = True
                    for neighbour in adj_list[node]:
                        if not visited[neighbour]:
                            queue.append(neighbour)
                count += 1
        return count

