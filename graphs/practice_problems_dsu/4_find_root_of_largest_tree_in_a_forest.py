#https://enginebogie.com/public/question/find-root-of-largest-tree-in-a-forest/2679

#N = total number of unique nodes in the forest.
#Time complexity: O(N * α(N)) -- practically O(N)
#Space Complexity: O(N)

class Solution:
    def largest_node_in_forest(self, n: int, edges: List[List[int]]) -> int:
        #adj_list as we don't know number of nodes for now 
        all_nodes = set()
        child_nodes = set()
        for u, v in edges:
            all_nodes.add(u)
            all_nodes.add(v)
            child_nodes.add(u)
        n = len(all_nodes)
        #let's assume for now that each node is its own parent
        parent = {node: node for node in all_nodes}

        #let's assume every element is its only component for now 
        size = {node: 1 for node in all_nodes}
        #we aren't taking ranking as we want to do only union by size 

        roots = all_nodes - child_nodes

        #first lets make findParent function

        def findparent(u,parent,size):
            if parent[u] != u:
                #This will also compress the whole component 
                parent[u] = findparent(parent[u],parent,size) 
            return parent[u]
        
        def unionbysize(u,v,parent,size):
            pu = findparent(u,parent,size)
            pv = findparent(v,parent,size)

            if pu == pv:
                return
            if size[pu] > size[pv]:
                 parent[pv] = pu
                 size[pu] += size[pv]
            elif size[pu] < size[pv]:
                 parent[pu] = pv
                 size[pv] += size[pu]
            else:
                parent[pu] = pv
                size[pv] += size[pu]

        for u,v in edges:
            unionbysize(u,v,parent,size)

        max_size = float('-inf')
        answer_root = -1
        for root in roots:
            p = findparent(root, parent, size)
            current_size = size[p]

            if current_size > max_size:
                max_size = current_size
                answer_root = root
            elif current_size == max_size:
                answer_root = min(answer_root, root)

        return answer_root


#-------------------
#https://enginebogie.com/public/question/find-root-of-tree-with-maximum-children-in-a-forest/2600


#Simple approach -- O(N) with just a hash_map:
def largest_node_in_forest(self, n, edges):
    roots = set()
    direct_children_count = defaultdict(int)

    for child, parent in edges:
        if parent == -1:
            roots.add(child)
        else:
            direct_children_count[parent] += 1

    best_root = None
    max_children = -1

    for root in roots:
        count = direct_children_count.get(root, 0)
        if count > max_children:
            max_children = count
            best_root = root

    return best_root