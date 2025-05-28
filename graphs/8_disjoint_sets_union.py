class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def findParent(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.findParent(self.parent[u])  # Path compression
        return self.parent[u]
    
    def find(self, u: int, v: int) -> bool:
        return self.findParent(u) == self.findParent(v)

#union by rank
    def unionByRank(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

#union by size
    def unionBySize(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]