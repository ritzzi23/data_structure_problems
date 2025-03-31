
class Solution:
    def reverseDLL(self, head):
        if head is None or head.next is None:
            return head
        curr,last = head, None
        
        while curr:
            last =  curr.prev
            curr.prev = curr.next
            curr.next = last 
            curr = curr.prev
            
        return last.prev 