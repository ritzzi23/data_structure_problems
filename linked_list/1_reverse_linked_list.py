#Reverse a singly linked list
#Time Complexity: O(n)
#Space Complexity: O(1) for iterative approach and O(n) for recursive approach due

from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next  = prev
            prev = curr
            curr = nxt
        return prev
#------------------------------
#Time Complexity: O(n)
#Space Complexity: O(n) for recursive approach


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)
        front = head.next 
        front.next = head
        head.next = None
        return  new_head
        
        