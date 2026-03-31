#Recursive Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right'

#Total Time Complexity: O(n)
#Total Space Complexity: O(h)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = [] #Space Complexity: O(h)
        def dfs(root): #Time Complexity: O(n)
            if not root:
                return []
            
            if root.left:
                dfs(root.left) #Time Complexity: O(n)
            result.append(root.val) #Time Complexity: O(1)
            if root.right:
                dfs(root.right) #Time Complexity: O(n)
        dfs(root) #Time Complexity: O(n)
        return result

#-------------------------------------------------------------------------------------
#Iterative using stack

#Total Time Complexity: O(n)
#Total Space Complexity: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [] #Space Complexity: O(h)
        result = [] #Space Complexity: O(h)
        curr = root
        if not curr: #Time Complexity: O(1)
            return []
        while curr or stack: #Time Complexity: O(n)
            while curr: #Time Complexity: O(n)
                stack.append(curr) #Time Complexity: O(1)
                curr = curr.left #Time Complexity: O(1)
            curr = stack.pop() #Time Complexity: O(1)
            result.append(curr.val) #Time Complexity: O(1)
            curr = curr.right
        return result


#-------------------------------------------------------------------------------------

#Morris Traversal

