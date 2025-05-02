from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nxt 
            return prev 
        def inter_addTwoNumbers(l1,l2):
            if not l1 and not l2:
                return [0]
            if not l1:
                return(l2)
            if not l2:
                return(l1)
            i = 0
            j = 0
            result = ListNode(0)
            curr = result
            carry_on = 0
            while (l1 or l2 or carry_on):
                x = (l1.val) if l1 else 0
                y = (l2.val) if l2 else 0
                temp = x + y + carry_on
                carry_on = temp //10
                curr.next = ListNode(temp % 10)
                curr = curr.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            return result.next
        l1 = reverse(l1)
        l2 = reverse(l2)
        return (reverse(inter_addTwoNumbers(l1, l2)))
        
            