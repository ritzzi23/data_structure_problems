from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        leftn = self.lowestCommonAncestor(root.left, p, q)
        rightn = self.lowestCommonAncestor(root.right, p, q)

        if leftn and rightn:
            return root
        
        if leftn:
            return leftn

        return rightn
#Time: O(n)
#Space: O(h) → O(n) in worst case, O(log n) in best case
        