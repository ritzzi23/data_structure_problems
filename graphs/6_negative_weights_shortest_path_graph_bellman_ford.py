class Solution:
    def bellman_ford(self, V, edges, S):
        distances = [int(1e9)] * V
        distances[S] = 0

        #distances all edges V-1 times
        for i in range(V-1):
            for u, v, w in edges:
                if distances[u] != int(1e9) and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
            
        #check for negative weight cycles 
        for u,v,w in edges:
            if distances[u] != int(1e9) and distances[u] + w < distances[v]:
                    return [-1]
        return distances