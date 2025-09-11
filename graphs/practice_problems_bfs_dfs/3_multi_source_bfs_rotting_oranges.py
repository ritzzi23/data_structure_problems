#Time Complexity: O(N*M) where N is the number of rows and M is the number of columns in the grid.
#Space Complexity: O(N*M) for the queue in the worst case when all oranges are
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Add all rotten oranges to queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(-1,0),(1,0),(0,1),(0,-1)]  # Up/North, Down/South, Right/East, Left/West
        time = 0

        # Step 2: BFS
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  
                    fresh -= 1
                    queue.append((nr, nc, t + 1))

        return time if fresh == 0 else -1
#--------------------------------------------------------------------------------------------
#Practice Problems using Multi-Source BFS:
#https://chatgpt.com/share/68a6ab21-de60-800c-a392-3b542790cf98
#https://leetcode.com/discuss/post/1833581/bfs-and-its-variations-by-c0d3m-o47u/

'''Walls and Gates
Medium
Battleships in a Board
Medium
Detonate the Maximum Bombs
Medium
Escape the Spreading Fire
Hard
'''


#------------------------------------------------------------------------------------------

'''Rotting Oranges
Walls and Gates
Shortest Distance from All Buildings
01 Matrix
As Far from Land as Possible
Shortest Path in Binary Matrix
Pacific Atlantic Water Flow
Number of Islands
Max Area of Island
Surrounded Regions'''