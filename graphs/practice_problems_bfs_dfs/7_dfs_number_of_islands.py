from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, columns = len(grid), len(grid[0])
        islands = 0

        def dfs_helper(i,j, rows, columns):
            #check if current positions if not valid
            if (i<0  or i>= rows) or (j<0 or j>= columns):
                return
            grid[i][j] = "0"
            directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
            stack = [(i,j)]
            while stack:
                r, c = stack.pop()
                for dx, dy in directions:
                    nx , ny = r + dx , c + dy
                    #check if the next cell is within bounds
                    if (0<= nx < rows) and (0<= ny < columns):
                        #check if the next cell is land and not visited
                        if grid[nx][ny] == "1":
                            #mark it visited
                            grid[nx][ny] = "0"
                            stack.append((nx, ny))

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    dfs_helper(i,j, rows, columns)
                    islands += 1
        return islands
#----------------------------------------------------------------------------

#RECURSIVE DFS APPROACH
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            # base case: out of bounds OR water
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return
            # mark as visited
            grid[i][j] = "0"
            # explore all 4 directions
            dfs(i - 1, j)  # up
            dfs(i + 1, j)  # down
            dfs(i, j - 1)  # left
            dfs(i, j + 1)  # right

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands

        