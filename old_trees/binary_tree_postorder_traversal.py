from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result

    def createTree(self, values: List[int]) -> Optional[TreeNode]:
        """Create a binary tree from a list of values (level-order traversal)."""
        if not values:
            return None
            
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Add left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Add right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
            
        return root
    
    def treeToList(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Convert a binary tree to a list (level-order traversal)."""
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
                
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
            
        return result

# Example usage
if __name__ == "__main__":
    values = [1, None, 2, 3]
    solution = Solution()
    
    # Create the tree from list
    root = solution.createTree(values)
    
    # Get postorder traversal
    postorder_result = solution.postorderTraversal(root)
    
    # Convert tree to list for visualization
    tree_list = solution.treeToList(root)
    
    # Print results
    print(f"Original tree (level-order): {tree_list}")
    print(f"Inorder traversal: {postorder_result}")
