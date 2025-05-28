from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            adj_list[u].append(v)

        for u in range(numCourses):
            for v in adj_list[u]:
                in_degree[v] += 1

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for v in adj_list[node]:

                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        if len(result) == numCourses:
            return True
        else:
            return False
        