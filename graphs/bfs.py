from collections import deque
def bfs_recursive(q):
    node = q.popleft()
    for nei_node in adj_list[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)
    bfs_recursive(q)

    





source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)
bfs_recursive(q)