from typing import List, Optional, defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return []
        #BFS to build to the undirected graph
        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        visited = set([start])
        max_count = 0
        q = deque([(start,0)])
        while q:
            node, row_val = q.popleft()
            max_count = max(max_count,row_val)
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh) 
                    q.append((neigh, row_val+1))
        return max_count

        