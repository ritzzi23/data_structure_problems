''' Practice Problems - BFS/DFS
Max Area of Island
Medium
Flood Fill
Easy
Coloring A Border'''

#Time Complexity: O(R × C)
#Space Complexity: O(R × C)
#bfs solution
from collections import deque
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
        queue = deque()
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    grid[i][j] = -1
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+ dx, y+dy
                if (
                    #check if the next cell is within bounds
                    (0<= nx<len(grid)) and 
                    (0<= ny <len(grid[0]))):
                        #check if the next cell is water or out of bounds
                        if (grid[nx][ny] == 0):
                            perimeter += 1
                        #check if the next cell is land and not visited
                        elif (grid[nx][ny] == 1):
                            queue.append((nx,ny))
                            grid[nx][nx] = -1
                #check if the next cell is out of bounds
                else:
                    perimeter += 1
        return perimeter 
#--------------------------------------------------------------------------------------------
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        # Check each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # Only process land cells
                if grid[i][j] == 1:
                    # Check all 4 directions
                    directions = [(-1,0), (1,0), (0,1), (0,-1)]
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        
                        # If neighbor is out of bounds or water, add to perimeter
                        if (ni < 0 or ni >= rows or nj < 0 or nj >= cols or 
                            grid[ni][nj] == 0):
                            perimeter += 1
        
        return perimeter