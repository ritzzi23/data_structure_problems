from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def height(node):
            if not node:
                return 0
            #self.max_sum = max(self.max_sum, self.max_sum + node.val)
            left_sum = max(height(node.left),0)
            right_sum = max(height(node.right),0)

            self.max_sum = max(self.max_sum,(node.val + left_sum + right_sum))

            return node.val + max(left_sum,right_sum)
        height(root)
        return self.max_sum


            
        
        
        