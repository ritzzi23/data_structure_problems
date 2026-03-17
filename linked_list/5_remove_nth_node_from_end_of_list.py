'''
Approach 1: HashMap (O(n) extra space)

If head is null, return null.

Create a dictionary mp to map: original_node -> copied_node.

First pass (build copies + next links):

Traverse the original list with curr.

For each original node, create a new node with the same value.

Store it in mp[curr].

Link the copied nodes using prev.next.

Second pass (set random links):

Traverse original and copied lists together.

For each original node:

If curr.random is null, set copy.random = null.

Else set copy.random = mp[curr.random] (jump to the copied version).

Return the head of the copied list.

Approach 2: Weaving (O(1) extra space)

If head is null, return null.

Pass 1 (weave copied nodes into original list):

Traverse original list with curr.

For each original node:

Create its copy node.

Insert the copy right after the original:

curr -> copy -> currNext

Pass 2 (assign random pointers for copies):

Traverse original list again, but jump two steps at a time.

For each original node curr:

If curr.random is null, set curr.next.random = null.

Else set curr.next.random = curr.random.next

Because curr.random.next is the copied node of the random target.

Pass 3 (unweave: separate the two lists):

newHead = head.next (first copied node).

Traverse both lists together:

Restore original list by skipping copy nodes.

Build copied list by skipping original nodes.

Return newHead.
'''