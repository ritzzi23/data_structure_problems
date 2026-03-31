#Approach 1: BFS Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Total Time Complexity: O(n)
#Total Space Complexity: O(n)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        level = 0
        while (queue):  #Time Complexity: O(n)
            current_level = [] #Space Complexity: O(n)
            for i in range(len(queue)): #Time Complexity: O(n)
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level[-1])
        return result
        
