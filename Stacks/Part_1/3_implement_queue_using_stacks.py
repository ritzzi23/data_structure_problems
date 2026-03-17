#Stack Operations using Queues
#Stacks are LIFO - Last In First Out
#Queues are FIFO - First In First Out

#Time Complexity: O(1) for push, amortized O(1) for pop and peek operations.
#Space Complexity: O(N) for storing queue elements in the stacks.

from collections import deque

class MyQueue:

    def __init__(self):
        #We will use two stacks to implement queue operations
        #stack1 will be used for enqueue operation
        self.stack1 = []
        #stack2 will be used for dequeue operation
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        #If stack2 is empty, we need to transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        #Now the top of stack2 is the front of the queue
        return self.stack2.pop()
    
    
    def peek(self) -> int:
        #similar to pop but we will not remove the element
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        #Now the top of stack2 is the front of the queue
        return self.stack2[-1]


    def empty(self) -> bool:
        #The queue is empty if both stacks are empty
        return len(self.stack1) == 0 and len(self.stack2) == 0
    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()