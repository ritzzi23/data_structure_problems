from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rotten = 0
        fresh = 0
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0)) # Include minute count
                    rotten += 1
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
        time = 0
        while queue:
            x, y, t = queue.popleft()
            time = max (t,time)
            
            for dx, dy in directions:
                nx, ny = x+ dx, y + dy
                if ((0 <= nx < len(grid)) and
                 (0 <= ny < len(grid[0])) and 
                 (grid[nx][ny] == 1)):
                 grid[nx][ny] = 2
                 fresh -= 1
                 queue.append((nx,ny,t+1))
        return time if fresh == 0 else -1 



