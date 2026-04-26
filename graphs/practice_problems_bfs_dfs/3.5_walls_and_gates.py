#Time 
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    #left,right,distance
                    node = (i,j,0)
                    queue.append(node)
        directions = [(-1,0),(1,0),(0,1),(0,-1)]  # Up/North, Down/South, Right/East, Left/West
        while queue:
            r,c,d = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = d+1
                    new_node = (nr,nc,d+1)
                    queue.append(new_node)
