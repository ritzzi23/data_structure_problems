class Solution:
    def bellman_ford(self, V, edges, S, is_undirected=False):
        distances = [int(1e9)] * V
        distances[S] = 0

        # Convert undirected edges to bidirectional if needed
        if is_undirected:
            new_edges = []
            for u, v, w in edges:
                new_edges.append([u, v, w])
                new_edges.append([v, u, w])
            edges = new_edges

        # Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if distances[u] != int(1e9) and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Check for negative-weight cycles
        for u, v, w in edges:
            if distances[u] != int(1e9) and distances[u] + w < distances[v]:
                return [-1]

        return distances
