class Solution:
    def infixtoPostfix(self, s):
        # Define operator precedence
        #BODMAS/BIDMAS rules
        # This dictionary defines the precedence of operators for conversion
        # Higher values indicate higher precedence
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = []
        stack = []
        for char in s:
            # If the character is an operand, add it to the output
            if char.isalnum():
                output.append(char)
            # If the character is '(', push it to the stack
            elif char == '(':
                stack.append(char)
            # If the character is ')', pop from stack to output until '(' is found
            elif char == ')':
                #check for empty stack to avoid error
                while stack and stack[-1] != '(':
                    # Pop from stack to output
                    output.append(stack.pop())
                # Pop the '(' from the stack
                if stack:
                    stack.pop()
            else:
                # If the character is an operator, pop from stack to output based on precedence
                while stack and stack[-1] != '(':
                    if char == '^' and (precedence[stack[-1]] > precedence[char]):
                        #For right associative operator '^', we only pop if the precedence is greater
                        output.append(stack.pop())
                    elif char != '^' and (precedence[stack[-1]] >= precedence[char]):
                        #While the operator on the stack has greater than or equal precedence to the current char,
                        #we must pop it from the stack and add it to the output
                        output.append(stack.pop())
                    else:
                        break
                # Push the current operator to the stack
                stack.append(char)
        #Now as loop finishes scanning the entire input string s, the stack might not be empty.
        #So we need to pop all remaining operators from the stack to the output
        while stack:
            output.append(stack.pop())
        #Join the output list to form the final postfix expression string
        return ''.join(output)
