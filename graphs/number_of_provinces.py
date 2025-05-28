from collections import defaultdict
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
        count = 0
        def dfs(city):
            for nei_node in adj_list[city]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    dfs(nei_node)

        seen = set()
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                count += 1
        return count

#==============================
from collections import defaultdict
from collections import deque
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
        count = 0
        seen = set()
        q = deque()
        def bfs_recursive(qu):
            if not qu:
                return
            node = qu.popleft()
            for nei_node in adj_list[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    qu.append(nei_node)
            bfs_recursive(qu)
        for i in range(n):
            if i not in seen:
                seen.add(i)
                q.append(i)
                bfs_recursive(q)
                count += 1
        return count 

