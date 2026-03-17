'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    if not root:
        return []
    
    result = [root.data]  # Add root
    
    # Get left boundary (excluding leaves)
    def left_boundary(node):
        if not node:
            return
        #to avoid the leaf nodes 
        if (not node.left and not node.right):
            return
        result.append(node.data)
        
        if node.left:
            left_boundary(node.left)
        elif node.right:
            left_boundary(node.right)
    
    # Get all leaf nodes from left to right
    def leaf_nodes(node):
        if not node:
            return
        
        if not node.left and not node.right:
            result.append(node.data)
            return
        
        leaf_nodes(node.left)
        leaf_nodes(node.right)
    
    # Get right boundary in reverse order (excluding leaves)
    def right_boundary(node):
        if not node:
            return
        #to avoid the leaf nodes 
        if (not node.left and not node.right):
            return
        if node.right:
            right_boundary(node.right)
        elif node.left:
            right_boundary(node.left)
        
        result.append(node.data)  # Add after recursive calls for reverse order
    
    # Process boundaries
    if root.left:
        left_boundary(root.left)
    
    # Process all leaf nodes
    leaf_nodes(root)
    
    # Process right boundary in reverse order (excluding root and leaves)
    if root.right:
        right_boundary(root.right)
    
    return result
#---------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = [root.val]

        def left_boundary(node):
            if not node or (not node.left and not node.right):
                return
            result.append(node.val)
            if node.left:
                left_boundary(node.left)
            else:
                left_boundary(node.right)

        def leaf_nodes(node):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
                return
            leaf_nodes(node.left)
            leaf_nodes(node.right)

        def right_boundary(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                right_boundary(node.right)
            else:
                right_boundary(node.left)
            right.append(node.val)  # Post-order: collect first, append later

        right = []
        if root.left:
            left_boundary(root.left)
        leaf_nodes(root)
        if root.right:
            right_boundary(root.right)
            result.extend(right)  # Add reversed right boundary

        return result
