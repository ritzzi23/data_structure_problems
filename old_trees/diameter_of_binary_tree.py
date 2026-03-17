from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Time: O(n)
#Space: O(h) → O(n) worst case, O(log n) best case
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = float('-inf')
        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            self.diameter = max(self.diameter,left_height + right_height)

            return max(left_height , right_height) + 1

        height(root)
        return self.diameter
        


