'''But for a tree to be balanced, 3 things must be true:

left subtree must be balanced
right subtree must be balanced
current node height difference must be at most 1'''

#Time Complexity: O(n)
#Space Complexity: O(h) where h is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #we are making a recursive function that will return two values
        #1. whether the subtree is balanced or not
        #2. height of the subtree
        #This can also be called as post order traversal
        def dfs(root): #Time Complexity: O(n)
            #Space Complexity: O(h) where h is the height of the tree
            #If the root is null then it is balanced and its height is 0
            if not root: 
                return True, 0
            #Recursively call for left and right subtrees
            left_balanced, left_height = dfs(root.left) #Time Complexity: O(n)
            right_balanced, right_height = dfs(root.right) #Time Complexity: O(n)

            #Check if the left and right subtrees are balanced and the height difference is at most 1
            balanced = left_balanced and right_balanced and abs(left_height-right_height) <= 1 #Time Complexity: O(1)
            #Calculate the height of the current node
            height = 1 + max(left_height , right_height)

            return balanced, height
        balanced, height = dfs(root) #Time Complexity: O(n)
        return balanced
        