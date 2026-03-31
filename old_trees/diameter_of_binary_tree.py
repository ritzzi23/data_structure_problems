#The answer is usually measured in number of edges, not number of nodes.

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we use a self variable because we need to update it throughout the recursion
        #and if we don't make it a class variable then the inside function will not be able to update the diameter
        self.diameter = float('-inf')
        #height function calculates the height of the tree
        def height(root):
            if not root:
                return 0
            #we recursively call height function for left and right subtree
            #we need the recursion to return the height of the subtree not the diameter
            left_height = height(root.left)
            right_height = height(root.right)
            #we update the diameter with the maximum of the current diameter and the sum of the heights of the left and right subtree
            #this is the diameter passing through the current node
            #we are calculating using edges not nodes 
            #because that will give us the diameter in terms of edges
            self.diameter = max(self.diameter,left_height + right_height)
            #we return the height of the current subtree
            #we add 1 to the height because we are adding the current node to the height
            return max(left_height , right_height) + 1

        height(root)
        return self.diameter
        


