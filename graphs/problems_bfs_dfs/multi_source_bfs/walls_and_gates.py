from collections import deque
from typing import List 
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        wall = 0
        gates = 0
        empty = 0
        INF = 2147483647
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j,0)) # gate is supposed to be no distance
                    gates += 1
                elif rooms[i][j] == INF:
                    empty += 1
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
        while queue:
            x,y,t = queue.popleft()

            for dx, dy in directions:
                nx, ny = x+ dx, y + dy
                if ((0 <= nx < len(rooms)) and
                 (0 <= ny < len(rooms[0])) and 
                 (rooms[nx][ny] == INF)):
                 rooms[nx][ny] = t+1
                 empty -= 1
                 queue.append((nx,ny,t+1))
        




        