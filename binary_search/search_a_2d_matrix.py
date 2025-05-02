from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end = (row * col) - 1
        while (start <= end):
            mid = start + (end-start)//2
            if (matrix[mid//col][mid%col] == target):
                return True
            elif (matrix[mid//col][mid%col] < target):
                start = mid + 1
            else:
                end = mid -1
        return False