#Time Complexity: O(N + E) where N is the number of nodes and E is the number of edges in the graph.
#Space Complexity: O(N) for the hashmap and the queue used in BFS."""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque([node])
        old_to_new = {node: Node(node.val)}

        while q:
            curr = q.popleft()
            for neigh in curr.neighbors:
                if neigh not in old_to_new:
                    old_to_new[neigh] = Node(neigh.val)
                    q.append(neigh)
                old_to_new[curr].neighbors.append(old_to_new[neigh])

        return old_to_new[node]
