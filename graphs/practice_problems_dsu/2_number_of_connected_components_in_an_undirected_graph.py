class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]

        def findParent(u, parent, size):
            if parent[u] != u:
                parent[u] = findParent(parent[u], parent, size)
            return parent[u]
        
        def unionBySize(u, v, parent, size):
            pu = findParent(u, parent, size)
            pv = findParent(v, parent, size)

            if pu == pv:
                return 

            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        for u, v in edges:
            unionBySize(u, v, parent, size)
        
        for i in range(n):
            if findParent(i, parent, size) == i:
                count += 1

        return count