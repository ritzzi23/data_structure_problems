from typing import List, Optional
from collections import defaultdict, deque
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    if not root:
        return []
    col_table = defaultdict(list)
    q = deque([(root,0)])

    while q:
        node, col_val = q.popleft()
        col_table[col_val] = (node.data)
        if node.left:
            q.append((node.left,col_val-1))
        if node.right:
            q.append((node.right,col_val+1))
    sorted_col_table = sorted(col_table.keys())
    return [col_table[col] for col in sorted_col_table]

#nothing much just updating all the column values with their last value encountered 