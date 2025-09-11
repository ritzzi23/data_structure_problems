#Time complexity: O(N^2)
#Space complexity: O(N) for visited array and O(N) for recursion stack in worst
#This is the BFS approach (Recursive) (Using Queue) (adjacency Matrix converted to adjacency list)
from collections import defaultdict, deque
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs_helper(queue,visited,adj_list):
            if not queue:
                return
            node = queue.popleft()
            visited[node] = True
            for neigh in adj_list[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    queue.append(neigh)
            bfs_helper(queue,visited,adj_list)

        adj_list = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        visited = [False] * len(adj_list)
        queue = deque()
        connected_provinces = 0

        for i in range(len(adj_list)):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                bfs_helper(queue,visited,adj_list)
                connected_provinces += 1
        return connected_provinces
#--------------------------------------------------------------------------------------------

from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs_helper(queue, visited):
            if not queue:
                return
            node = queue.popleft()
            visited[node] = True
            for neigh in range(n):                     # ✅ directly check matrix
                if isConnected[node][neigh] == 1 and not visited[neigh]:
                    visited[neigh] = True
                    queue.append(neigh)
            bfs_helper(queue, visited)                 # recursion continues BFS

        n = len(isConnected)
        visited = [False] * n
        queue = deque()
        connected_provinces = 0

        for i in range(n):
            if not visited[i]:
                queue.append(i)
                bfs_helper(queue, visited)
                connected_provinces += 1

        return connected_provinces
