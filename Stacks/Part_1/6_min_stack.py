#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#Time Complexity: O(1) for all operations
#Space Complexity: O(N) where N is the number of elements in the stack

class MinStack:

    def __init__(self):
        #We will use two stacks: one for all elements and another for tracking minimums
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        #For the push operation, we add the value to the main stack
        self.stack.append(val)
        #We also check if we need to update the min_stack
        #we check if the min_stack is empty or if the new value is less than or equal to the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        #For the pop operation, we remove the top element from the main stack
        if self.stack:
            val = self.stack.pop()
            #If the popped value is the same as the current minimum, we also pop it from the min_stack
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        #The top operation returns the top element of the main stack
        if self.stack:
            return self.stack[-1]
        return None
        
    def getMin(self) -> int:
        #The getMin operation returns the top element of the min_stack, which is the current minimum
        if self.min_stack:
            return self.min_stack[-1]
        return None
    

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()