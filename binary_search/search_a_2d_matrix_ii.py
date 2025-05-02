from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col- 1
        while (i>=0 and i< row) and (j>=0 and j< col):
            if (matrix[i][j] == target):
                return True
            elif (matrix[i][j] > target):
                j -= 1
            else:
                i += 1
        return False