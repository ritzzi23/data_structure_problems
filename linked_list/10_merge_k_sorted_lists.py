# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time Complexity: O(N log N) where N is the total number of nodes across all lists.
#Space Complexity: O(N) for storing all node values.
#brute force approach
from typing import List, Optional 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #we will define a brute force approach here
        #check all values seuquentially and add them to a new list
        all_values = []
        for head in lists:
            current = head
            while current:
                all_values.append(current.val)
                current = current.next
        #sort all values
        all_values.sort()
        #create a new linked list from sorted values
        dummy = ListNode(0)
        current = dummy
        for val in all_values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next  

#------------------------------

#Time Complexity: O(N log k) where N is the total number of nodes across all lists and k is the number of lists.
#Space Complexity: O(k) for the min-heap.


#Optimal Approach using Min-Heap
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        #initialize the heap with the head nodes of each list
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        #Now we will extract the minimum element from the heap and add it to the merged list
        dummy = ListNode(0)
        current = dummy
        while min_heap:
            val, list_index, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            #Now as the Linkedlist is in ascending order we will move to the next node in the same list
            # and add it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))
            #move current pointer
            current = current.next
        return dummy.next
    