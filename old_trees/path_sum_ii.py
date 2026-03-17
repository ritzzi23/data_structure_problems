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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node,currPath,currSum):
            if not node:
                return False
            currPath.append(node.val)
            currSum += node.val
            if not node.left and not node.right:
                if currSum == targetSum:
                    result.append(list(currPath))
            else:
                dfs(node.left,currPath,currSum)
                dfs(node.right,currPath,currSum)
            currPath.pop()

        dfs(root,[],0)
        return result