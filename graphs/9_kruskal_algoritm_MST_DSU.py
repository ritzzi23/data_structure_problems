from typing import List
class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []
        
    def find(self,x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    #union by rank    
    def union(self,x,y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent == y_parent:
            return
        
        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1
        
        
    def kruskal(self,edges):
        mst_weights = 0
        for u,v,wt in edges:
            parent_u = self.find(u)
            parent_v = self.find(v)
            
            if (parent_u != parent_v):
                self.union(u,v)
                mst_weights += wt
        return mst_weights
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        self.parent = [x for x in range(V)]
        self.rank = [0] * V
        
        edges = []
        for u in range(V):
            for v, wt in adj[u]:
                edges.append((u,v,wt))
        
        edges.sort(key = lambda x:x[2])
        
        return self.kruskal(edges)
        