from collections import defaultdict, deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(i,j):
            if (i< 0 or i >=len(grid) or
            j< 0 or j >=len(grid[0]) or
            grid[i][j] != "1"):
                return 

            grid[i][j] = "0"

            que = deque([(i,j)])
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while que:
                row, col = que.popleft()
                for dx, dy in directions:
                    next_row, next_col = row+ dx, col + dy
                    if (0<=next_row<len(grid) and
                        0<=next_col<len(grid[0]) and
                            grid[next_row][next_col] == "1" ):
                                grid[next_row][next_col] = "0"
                                que.append((next_row,next_col))

        n = len(grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count += 1
        return count


        