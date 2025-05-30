from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
        m, n = len(mat), len(mat[0])
        dist = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
        while queue:
            x, y = queue.popleft()
            for dx,dy in directions:
                nx, ny = x + dx, y +dy
                if (    
                    (0<= nx < len(mat))
                            and 
                    (0<= ny < len(mat[0]))
                    and
                    (dist[nx][ny] == -1)
                    ):
                        dist[nx][ny] = dist[x][y] + 1
                        #we need to append this because this will help us find distance of ones that are only surround by 1s
                        queue.append((nx,ny))
        return dist

#===========================================
#now doing it with O(1) space

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
        m, n = len(mat), len(mat[0])
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = float('inf')  
        while queue:
            x, y = queue.popleft()
            for dx,dy in directions:
                nx, ny = x + dx, y +dy
                if (
                    (0<= nx < len(mat)) and (0<= ny < len(mat[0]))
                    ):
                        #we are checking if the next term is inf or not 
                        if (mat[nx][ny] > mat[x][y]+1):
                            mat[nx][ny] = mat[x][y] + 1
                            #we need to append this because this will help us find distance of ones that are only surround by 1s
                            queue.append((nx,ny))
        return mat

