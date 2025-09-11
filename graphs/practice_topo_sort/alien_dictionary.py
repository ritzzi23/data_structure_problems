#Time Complexity: O(C) where C is the total number of characters in the words list.
#Space Complexity: O(1) since the graph can have at most 26 nodes (lowercase English letters).

#https://chatgpt.com/share/68bd1b89-52f0-8000-aead-3d4ca411ae5e

from collections import defaultdict, deque
from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def build_graph(words):
            graph = defaultdict(list)
            indegree = {}
# Initialize indegree for all unique characters
            for w in words:
                for c in w:
                    indegree[c] = 0
# Build graph edges based on the order of characters in adjacent words            
            for i in range(len(words)-1):
                w1, w2 = words[i], words[i+1]

#invalid case like ("abc","ab")
                if len(w1) > len(w2) and w1[:len(w2)] == w2:
                    return None, None
# Find the first differing character and create a directed edge
                for c1,c2 in zip(w1,w2):
                    if c1 != c2:
                        graph[c1].append(c2)
                        indegree[c2] += 1
                        break
            return graph, indegree
        
# Topological Sort using Kahn's Algorithm
        def topo_sort(graph,indegree):
            queue = deque()
            for char in indegree:
                if indegree[char] == 0:
                    queue.append(char)
            
            #topo_sort
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1

                    if indegree[neigh] == 0:
                        queue.append(neigh)
# If result length is less than total unique characters, a cycle exists                        
            if len(result) < len(indegree):
                return ""
            return result

        graph, indegree = build_graph(words)
#if graph is None:   # Invalid prefix case detected
        if graph is None:   # invalid prefix case
            return ""   

        result = topo_sort(graph,indegree)
#return the result as a string
        return "".join(result) if result else ""
