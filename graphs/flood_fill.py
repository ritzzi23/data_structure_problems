from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # If the starting pixel is already the new color, return the original image
        if image[sr][sc] == color:
            return image
        
        def dfs(grid, i, j, old_color, new_color):
            # Check boundaries and whether the current cell matches old_color
            if (i < 0 or i >= len(grid) or 
                j < 0 or j >= len(grid[0]) or 
                grid[i][j] != old_color):
                return
            
            # Update the color of the current cell
            grid[i][j] = new_color
            
            # Recursively call dfs on the four adjacent cells
            dfs(grid, i + 1, j, old_color, new_color)
            dfs(grid, i - 1, j, old_color, new_color)
            dfs(grid, i, j + 1, old_color, new_color)
            dfs(grid, i, j - 1, old_color, new_color)
        
        # Store the original color of the starting pixel
        old_color = image[sr][sc]
        
        # Start the depth-first search from the given starting point
        dfs(image, sr, sc, old_color, color)
        
        return image