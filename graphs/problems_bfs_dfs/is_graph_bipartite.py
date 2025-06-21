from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs_helper(graph,node,colors,cur_color):
            colors[node] = cur_color
            for neigh in graph[node]:
                if(colors[neigh] == cur_color):
                    return False
                elif(colors[neigh] == -1):
#                    colors[neigh] = 1- cur_color
                    if not dfs_helper(graph,neigh,colors,1- cur_color):
                        return False
            return True 


        colors = [-1] * len(graph)
        for i in range(len(graph)):
            if (colors[i] == -1):
                if not dfs_helper(graph,i,colors,1):
                    return False
        return True

#-------------------------------------------------------------------------------------------
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs_helper(i,graph,color,curr_color):
            color[i] = curr_color
            queue = deque([i])
            
            while queue:
                node = queue.popleft()
                for neigh in graph[node]:
                    if (color[neigh] == color[node]):
                        return False
                    elif (color[neigh] == -1):
                        color[neigh] = 1 - color[node]
                        queue.append(neigh) 
            return True

        color = [-1] * len(graph)
        for i in range(len(graph)):
            if (color[i] == -1):
                if not bfs_helper(i,graph,color,1):
                    return False
        return True
    
        