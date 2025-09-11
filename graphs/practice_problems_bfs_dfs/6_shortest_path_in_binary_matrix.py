#Time Complexity : O(N^2) where N is the number of rows or columns in the grid
#Space Complexity : O(N^2) for the queue in the worst case

from collections import deque
from typing import List 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)] #Up/North, Down/South, Right/East, Left/West
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        queue.append((0,0))
        # Edge case: start or end is blocked
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        grid[0][0] = 1  # mark visited        
        result = 1
        
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == rows-1 and c == cols-1:
                    return result
                for dx, dy in directions:
                    nx,ny = dx + r, dy + c
                    if(0<= nx < rows) and (0<= ny < cols) and (grid[nx][ny] == 0):
                        queue.append((nx,ny))
                        grid[nx][ny] = 1
            result += 1
        return -1



        