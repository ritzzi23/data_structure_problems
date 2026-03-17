#Stack Operations using Queues
#Stacks are LIFO - Last In First Out
#Queues are FIFO - First In First Out
#We will use two queues to implement stack operations, 
#because a single queue does not provide direct access to the last element added.
#Time Complexity: O(1) for push, O(N) for pop and top operations.
#So total time complexity is O(N) for pop and top operations.
#Space Complexity: O(N) for storing stack elements in the queues.

from collections import deque
class MyStack:

    def __init__(self):
        #Queue1 will be the main queue to hold stack elements
        self.queue1 = deque()
        #Queue2 will be used as a temporary queue for operations
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        #We need to remove the last element added to the stack
        #For this we will transfer all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        #The last element in queue1 is the top of the stack
        top_element = self.queue1.popleft()
        #Now we will swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element    

    def top(self) -> int:
        #Similar to pop but we will not remove the last element
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        top_element = self.queue1.popleft()


        #We need to add the top element back to queue2
        self.queue2.append(top_element)
        
        
        #Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element


    def empty(self) -> bool:
        #Check if queue1 is empty
        return len(self.queue1) == 0
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()