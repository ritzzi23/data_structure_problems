#Approach 1: DFS + level tracking



#Dry Run : [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]

#Approach 2: BFS + Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Total Time Complexity: O(n)
#Total Space Complexity: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root]) #Space Complexity: O(n)
        level = 0

        while(queue): #Time Complexity: O(n)
            current_level = [] #Space Complexity: O(n)
            for i in range(len(queue)): #Time Complexity: O(n)
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
        


            
        
