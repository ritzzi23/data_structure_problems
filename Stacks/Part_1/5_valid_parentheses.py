#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        #stack to keep track of opening brackets
        stack = []
        #mapping of closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                #check if the top of the stack matches the corresponding opening bracket and stack is not empty 
                #what if stack is empty? 
                #In that case, we can assume it is not valid
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                #push opening brackets onto the stack
                stack.append(char)
        
        return True if not stack else False
