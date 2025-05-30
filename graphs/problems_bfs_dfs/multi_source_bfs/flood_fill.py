from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        directions = [(-1,0),(1,0),(0,1),(0,-1)] #Up/North, Down/South, Right/East, Left/West
        queue = deque([(sr,sc)])
        image[sr][sc] = color
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx, ny = dx +x, dy + y
                if ((0<= nx < len(image)) 
                and (0<= ny < len(image[0])) 
                and (image[nx][ny] == original_color)):

                    image[nx][ny] = color 
                    queue.append((nx,ny))

        return image
