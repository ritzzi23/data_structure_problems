#Time Complexity of the code: O(1) for both get and put operations.
#Space Complexity: O(N) where N is the capacity of the cache.
# Definition for doubly linked list node.
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1  #frequency of access
        self.prev = None
        self.next = None

#Node for doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  #dummy head
        self.tail = Node(0, 0)  #dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

#https://gemini.google.com/share/16914dd84cd2
    def add_to_front(self, node: Node) -> None:
        #make previous of new node point to head
        node.prev = self.head
        #make next of new node point to current first node
        node.next = self.head.next
        #make previous of current first node point to new node
        self.head.next.prev = node
        #make next of head point to new node
        self.head.next = node
        #increment size
        self.size += 1

    def remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_last(self) -> Node:
        if self.size > 0:
            last_node = self.tail.prev
            self.remove_node(last_node)
            return last_node
        return None



class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node = {} #key to node mapping
        self.freq_map = {} #frequency to doubly linked list mapping

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        # update the node's frequency
        self._update(node)
        return node.val

    def _update(self, node: Node) -> None:
        # remove node from current freq list
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        # if current list is empty and freq is min_freq, increment min_freq
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        # increase node's frequency
        node.freq += 1
        # add node to new freq list
        if node.freq not in self.freq_map:
            # create a new freq list if it doesn't exist
            self.freq_map[node.freq] = DoublyLinkedList()
        # add node to the front of the new freq list
        self.freq_map[node.freq].add_to_front(node)

    def put(self, key: int, value: int) -> None:
        # if capacity is 0, do nothing
        if self.capacity == 0:
            return
        # if key is already in cache, update the value and frequency
        if key in self.key_node:
            # update the value
            node = self.key_node[key]
            node.val = value
            # update the node's frequency
            self._update(node)
            return
        # if cache is at capacity, remove the least frequently used node
        if len(self.key_node) >= self.capacity:
            # get the least frequently used list (doubly linked list) with respect to min_freq
            lfu_list = self.freq_map[self.min_freq]
            # remove the least recently used node from this list
            lfu_node = lfu_list.remove_last()
            # remove it from key_node mapping
            del self.key_node[lfu_node.key]

        # Now for a new key, create a new node
        new_node = Node(key, value)
        # add it to key_node mapping
        self.key_node[key] = new_node
        # add it to freq_map with frequency 1
        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()
        # add the new node to the front of freq 1 list
        self.freq_map[1].add_to_front(new_node)
        # reset min_freq to 1
        self.min_freq = 1