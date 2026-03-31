# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time Complexity: O(n)
#Space Complexity: O(log n)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left,right): #Time Complexity: O(n)
            #Base case
            if left > right:
                return None
            #We are taking the middle element as the root
            mid = (left + right) //2 #Time Complexity: O(1)
            root = TreeNode(nums[mid]) #Time Complexity: O(1)

            root.left = build(left, mid-1) #Time Complexity: O(n)
            root.right = build(mid + 1 , right) #Time Complexity: O(n)

            return root
        root = build(0,len(nums)-1)
        return root        