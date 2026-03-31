# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Height of the tree is 1 + max(height of left subtree, height of right subtree)
    def height(node):
        #Base case
        if node is None:
            return 0

        #Recursive step
        #We are calculating the height of the left subtree
        #we recursively pass left child of the current node to get the leftmost depth of the tree
        left_height = height(node.left)
        #We are calculating the height of the right subtree
        #we recursively pass right child of the current node to get the rightmost depth of the tree
        right_height = height(node.right)

        #Return the height of the tree
        #if left height is greater than right height then return left height + 1
        
        if left_height > right_height:
            return left_height + 1
        else:
                return right_height + 1