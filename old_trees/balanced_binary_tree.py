from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            l_hei, l_bal = dfs(root.left)
            r_hei, r_bal = dfs(root.right)

            balanced = l_bal and r_bal and abs(l_hei-r_hei) <= 1
            height = max(l_hei,r_hei) + 1

            return height, balanced
        

        height, isBalanced = dfs(root)
        return isBalanced
        