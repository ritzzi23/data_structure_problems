#Time Complexity: O(n + m), where n and m are the lengths of list1 and list2 respectively.
#Space Complexity: O(1), since we are only using a constant amount of extra space

from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next 
        #check if any list has remaining nodes    
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

        

        
list1 = [1,2,4] 
list2 = [1,3,5]
a = Solution()
print(a.mergeTwoLists(list1,list2))        