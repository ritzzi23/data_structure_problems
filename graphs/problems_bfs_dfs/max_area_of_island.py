from collections import deque
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = deque()
        total_area = 0
        current_area = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    grid[i][j] = -1
                    current_area = 1
        
                while queue:
                    
                    x, y = queue.popleft()
                    for dx,dy in  directions:
                        nx, ny = x + dx, y + dy
                        if (
                            (0<= nx < len(grid))
                            and 
                            (0<= ny < len(grid[0]))
                        ):
                            if (grid[nx][ny] == 1):
                                queue.append((nx,ny))
                                grid[nx][ny] = -1
                                current_area += 1
                total_area = max(total_area,current_area)
        return total_area

                    

        