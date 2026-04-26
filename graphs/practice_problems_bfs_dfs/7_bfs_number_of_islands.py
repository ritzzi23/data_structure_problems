#time Complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid.
#space Complexity: O(min(M,N)) for the queue in the worst case.
#best solution
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, columns = len(grid), len(grid[0])
        islands = 0

        def bfs_helper(i,j, rows, columns):
            #check if current positions if not valid
            if (i<0  or i>= rows) or (j<0 or j>= columns):
                return

            grid[i][j] = "0"
            que = deque([(i,j)])
            directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
            while que:
                r, c = que.popleft()
                for dx, dy in directions:
                    nx , ny = r + dx , c + dy
                    #check if the next cell is within bounds
                    if (0<= nx < rows) and (0<= ny < columns):
                        #check if the next cell is land and not visited
                        if grid[nx][ny] == "1":
                            #mark it visited
                            grid[nx][ny] = "0"
                            que.append((nx,ny))

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    bfs_helper(i,j, rows, columns)
                    islands += 1
        return islands

#--------------------------------------------------------------------------
#RECURSIVE DFS APPROACH
# Time Complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid.
# Space Complexity: O(M * N) in the worst case due to recursion depth (when the entire grid is land).

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        islands = 0

        def dfs_helper(i, j):
            # base case: out of bounds OR water
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != "1":
                return
            # mark as visited
            grid[i][j] = "0"

            # explore all 4 directions
            dfs_helper(i - 1, j)  # Up
            dfs_helper(i + 1, j)  # Down
            dfs_helper(i, j - 1)  # Left
            dfs_helper(i, j + 1)  # Right

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    dfs_helper(i, j)
                    islands += 1

        return islands
#----------------------------------------------------------------------
#Time Complexity: O(m∗n∗α(m∗n)) approximately O(M*N)
#Space Complexity: O(M * N) for the parent and rank arrays
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        parent = [k for k in range(rows* cols)]
        rank = [1 for _ in range(rows*cols)]   
        count = [0] 

        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union_by_rank(a, b):
            pa = find_parent(a)
            pb = find_parent(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pa] = pb
                rank[pb] += 1
            count[0] -= 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count[0] += 1
                    idx = i * cols + j
                    if j + 1 < cols and grid[i][j + 1] == '1':
                        union_by_rank(idx, i * cols + (j + 1))
                    if i + 1 < rows and grid[i + 1][j] == '1':
                        union_by_rank(idx, (i + 1) * cols + j)

        return count[0]


        

        