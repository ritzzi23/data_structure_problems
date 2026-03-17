#Stack Operations using Array
#LIFO - Last In First Out

class MyStack:

    def __init__(self,capacity: int = 100) -> None:
        self.stack = []
        self.capacity = capacity
        # Initialize top pointer, it will point to the index of the top element in the stack
        self.top = -1

    def is_empty(self):
        # Check if the stack is empty
        # If top is -1, stack is empty
        return self.top == -1
    
    def is_full(self):
        # Check if the stack is full
        # If top is equal to capacity - 1, stack is full
        return self.top == self.capacity - 1
    
    def push(self, item):
        # Add an item to the top of the stack
        if self.is_full():
            raise Exception("Stack Overflow")
            # Stack is full, cannot push new item
            return False
        self.stack.append(item)
        self.top += 1
        return True
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
            return None
        popped_item = self.stack.pop()
        self.top -= 1
        return popped_item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
            return None
        return self.stack[self.top]
    
    def size(self):
        return self.top + 1
    
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        for i in range(self.top, -1, -1):
            print(self.stack[i])


# Example usage:
if __name__ == "__main__":
    my_stack = MyStack(5)
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.display()  # Output: 30 20 10
    print("Top element is:", my_stack.peek())  # Output: Top element is: 30
    print("Popped element is:", my_stack.pop())  # Output: Popped element is: 30
    my_stack.display()  # Output: 20 10
    print("Stack size is:", my_stack.size())  # Output: Stack size is: 2