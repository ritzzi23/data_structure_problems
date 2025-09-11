#Time Complexity: O(V + E)
#Space Complexity: O(V + E)
from collections import defaultdict, deque
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph = defaultdict(list)
        V = len(graph)


        #outdegree_creation
        outdegree = [0] * V
        for u in range(V):
            outdegree[u] = len(graph[u])
        #making reverse connections
            for v in graph[u]:
                rev_graph[v].append(u) 

        #queue_fill
        queue = deque()
        for i in range(V):
            if outdegree[i] == 0:
                queue.append(i)

        #topo sort
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neigh in rev_graph[node]:
                outdegree[neigh] -= 1

                if outdegree[neigh] == 0:
                    queue.append(neigh)
        return sorted(result)
#------------------------------------------------------------------------------------------------------------------

# Terminal node: no outgoing edges: graph[i] == []
# Safe node: Every path from i ends in a terminal node (or safe node).

# Goal: Return a list of all safe nodes, sorted in ASC order.

# Brute-force:
#   * For each node i, dfs with backtracking to either: 
#       (1) find a cycle, or 
#       (2) find terminal node.
#   * if node is is safe (or terminal) then add to ret.
#   * backtrack to set state safe, terminal, or unsafe, based on the 
#     state of neighbors.
# Notes:
#   * Once a terminal node is found, then it can be marked terminal.
#   * A node is only safe if ALL paths end in terminal/safe nodes.
#   * When a node is found to be safe, it can be marked safe.
#
#  Alternative #1: Union-find DSU
#   * One pass through graph to union all connected nodes.
#   * Terminal nodes are the root???
#   * In: [[1, 2, 3, 4], [0, 2, 3, 4]]
#   * Union every node. Return bool from Union if it's a cycle. 
#   * Record all nodes that would make a cycle.
#
#  Alternative #2: Reversed graph topo sort.
#   * Reversing the graph gives all terminal nodes indegree == 0.
#   * We run a Kahn's topo sort and store all nodes with indegree==0 to our output list.
#   * Sort the output list and return it.
#   * Time: O((|V| + |E|) + |V|*log(|V|))
#   * Space: O(|V| + |E|)

