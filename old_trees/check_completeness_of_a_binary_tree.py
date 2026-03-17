from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Time: O(n)
#Space: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        prev_node = False
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                prev_node = True
            else:
                if prev_node:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True


                    
                    
            

        