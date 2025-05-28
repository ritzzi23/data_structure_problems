from collections import deque
from typing import List


#DFS 
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(u,v,adj_list,visited):            
            if u == v:
                return True
            visited[u] = True
            for neigh in adj_list[u]:
                if not visited[neigh]:
                    if dfs(neigh,v,adj_list,visited):
                        return True
            return False
        adj_list = [[] for _ in range(numCourses)]
        #make adj list 
        for u,v in prerequisites:
            adj_list[u].append(v)
        result = []
        visited = [False] * numCourses
        for u,v in queries:
            visited = [False] * numCourses
            result.append(dfs(u,v,adj_list,visited))
        return result

#------------------------------------___-----------------------------

#BFS

from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def bfs(u,v,adj_list,visited):  
            q = deque([u])
            visited[u] = True
            while q:
                node = q.popleft()
                for neigh in adj_list[node]:
                    if neigh == v:
                        return True
                    if not visited[neigh]:
                        visited[neigh] = True
                        q.append(neigh)  
            return False

        adj_list = [[] for _ in range(numCourses)]
        #make adj list 
        for u,v in prerequisites:
            adj_list[u].append(v)
        result = []
        visited = [False] * numCourses
        for u,v in queries:
            visited = [False] * numCourses
            result.append(bfs(u,v,adj_list,visited))
        return result


#------------------------------------___-----------------------------


