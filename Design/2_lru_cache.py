#Brute Force Approach using List
#Time Complexity: O(N) for both get and put operations in worst case.
#Space Complexity: O(N) where N is the capacity of the cache.
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = []  # list of (key, value)
        self.n = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                val = self.cache[i][1]
                temp = self.cache[i]
                self.cache.pop(i)          # remove from current position
                self.cache.append(temp)    # move to most recent (end)
                return val
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)                # remove old
                self.cache.append((key, value))  # add as most recent
                return

        if len(self.cache) == self.n:
            self.cache.pop(0)                    # evict least recent (front)
        self.cache.append((key, value))          # add as most recent
#==========================================================================================

#Optimal Approach using Double Linked List and HashMap
#Time Complexity: O(1) for both get and put operations.
#Space Complexity: O(N) where N is the capacity of the cache.

#We make a class for the doubly linked list nodes.
class Node:
    def __init__(self,key: int, val: int):
        #key is the key of the cache entry
        #val is the value of the cache entry
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self,capacity: int):
        self.capacity = capacity
        #let's create hashmap to store key and node reference pairs
        self.cache = {}

        #create dummy head and tail nodes
        self.head = Node(0,0) #most recently used
        self.tail = Node(0,0) #least recently used
        self.head.next = self.tail #initially head points to tail
        self.tail.prev = self.head #tail points to head

    def _remove(self,node: Node) -> None:
        #removes a node from the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self,node: Node) -> None:
        #adds a node right after the head (most recently used position)
        node.prev = self.head
        node.next = self.head.next
        #Now the node is at the front
        #next we need to update the previous first node's prev to point to the new node
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        #if key is not in cache, return -1
        if key not in self.cache:
            return -1
        #if key is in cache, retrieve the node
        node = self.cache[key]
        #move the accessed node to the front (most recently used)
        self._remove(node)
        self._add_to_front(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        #if key is already in cache, update the value and move it to front
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
            return
        #if key is not in cache, create a new node
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        #if cache exceeds capacity, remove the least recently used item
        if len(self.cache) > self.capacity:
            #least recently used node is the one before tail
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]  #remove from hashmap
#==========================================================================================




