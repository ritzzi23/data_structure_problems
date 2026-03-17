from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            semi_result = []
            for i in range(len(q)):
                node = q.popleft() 
                semi_result.append(node.val)               
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(semi_result[-1])
        return result


#---------------------------------------------------------------
