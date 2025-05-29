from collections import defaultdict
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
        
        def dfs_helper(node,visited, adj_list):
            visited[node] = True
            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    dfs_helper(neighbour,visited, adj_list)


        visited = [False] * len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs_helper(i,visited, adj_list)
                count += 1
        return count

