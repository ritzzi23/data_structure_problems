from typing import List, Optional, defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_list = []
        q = deque([(root,0,0)])

        while q:
            node, row_val ,col_val = q.popleft()
            node_list.append((col_val, row_val, node.val))

            if node.left:
                q.append((node.left, row_val+1, col_val-1))
            if node.right:
                q.append((node.right, row_val+1, col_val+1))
        
        node_list.sort(key=lambda x:(x[0],x[1],x[2]))
        col_table = defaultdict(list)
        for col, row, value in node_list:
            col_table[col].append(value)
        sorted_col_table = sorted(col_table.keys())
        return [col_table[col] for col in sorted_col_table]

'''
node_list.sort(key=lambda x:(x[0],x[1],x[2]))
This means:
first sort by col
if same col, sort by row
if same row and col, sort by value

That is exactly the ordering required by the problem.'''




#--------------------------------------------------------------------------
#Issue with sorting of row values


from typing import List, Optional, defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col_table = defaultdict(list)
        q = deque([(root,0)])

        while q:
            node, col_val = q.popleft()
            col_table[col_val].append(node.val)

            if node.left:
                q.append((node.left,col_val-1))
            if node.right:
                q.append((node.right,col_val+1))
        sorted_col_table = sorted(col_table.keys())
        return [col_table[col] for col in sorted_col_table]