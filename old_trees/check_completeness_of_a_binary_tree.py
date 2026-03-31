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
            #if we encounter a null node then we set the prev_node to True
            #and if we encounter a non null node after that then the tree is not complete
            if node is None:
                prev_node = True
            else:
                if prev_node:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True


'''You are doing level order traversal and checking this rule:

once a None position appears,
every later position in BFS must also be None
if a real node appears after that, the tree is not complete

That is exactly the correct property of a complete binary tree.'''
                    
#--------------------------------------------


from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n)
# Space: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        seen_null = False
        q = deque([root])

        while q:
            node = q.popleft()
            #if we encounter a null node then we set the seen_null to True
            if node is None:
                seen_null = True
            else:
                #if we encounter a non null node after that then the tree is not complete
                if seen_null:
                    return False
                q.append(node.left)
                q.append(node.right)

        return True
            

        