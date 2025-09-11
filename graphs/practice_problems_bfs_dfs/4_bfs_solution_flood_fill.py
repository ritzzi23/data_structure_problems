#Time Complexity: O(R × C)
#Space Complexity: O(R × C)
from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image  # Nothing to do
        
        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color
        directions = [(-1,0),(1,0),(0,1),(0,-1)]  # Up/North, Down/South, Right/East, Left/West

        while queue:
            x,y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    (0<= nx <rows)
                    and 
                    (0<= ny < cols)
                    and 
                    (image[nx][ny] == original_color)
                ):
                    image[nx][ny] = color
                    queue.append((nx,ny))
        return image
#--------------------------------------------------------------------------------------------