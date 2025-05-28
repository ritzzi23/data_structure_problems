def dfs_recursive(node):
    print(node)
    for nei_node in adj_list[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)





source = 0
seen = set()
seen.add(source)
dfs_recursive(source)
stack = [source]
while stack:
    node = stack.pop()
    print(node)
    for nei_node in adj_list[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)

