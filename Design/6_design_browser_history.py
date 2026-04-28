# Design Browser History (LeetCode 1472)
# You have a browser of one tab where you start on the homepage and you can
# visit another url, get back in the history number of steps or move forward
# in the history number of steps.
#
# Implement the BrowserHistory class:
#   BrowserHistory(homepage)  - Initializes with the homepage of the browser.
#   visit(url)                - Visits url from the current page. Clears all forward history.
#   back(steps)               - Move steps back in history. Return current url.
#   forward(steps)            - Move steps forward in history. Return current url.

#==========================================================================================

# Approach 1: List + Truncate (Array-based) — Most Intuitive
# - Maintain a list of URLs and a current index pointer
# - visit(url): truncate everything after current, append new URL, increment pointer
# - back(steps): move pointer left by min(steps, current)
# - forward(steps): move pointer right by min(steps, last_valid_index - current)
# Time Complexity: visit O(n) worst case due to list slicing, back/forward O(1)
# Space Complexity: O(n)


#==========================================================================================

# Approach 2: Two Stacks
# - Use a back_stack and a forward_stack; keep current URL separately
# - visit(url): push current onto back_stack, set current = url, clear forward_stack
# - back(steps): pop from back_stack, push onto forward_stack, repeat up to steps times
# - forward(steps): pop from forward_stack, push onto back_stack, repeat up to steps times
# Time Complexity: visit O(1), back/forward O(steps)
# Space Complexity: O(n)


#==========================================================================================

# Approach 3: Doubly Linked List — Classic Design Pattern
# - Each node holds a URL with prev and next pointers
# - visit(url): create new node, link it after current, sever the forward chain
# - back(steps): walk prev pointers up to steps times
# - forward(steps): walk next pointers up to steps times
# Time Complexity: visit O(1), back/forward O(steps)
# Space Complexity: O(n)
# No array resizing, true O(1) insertion


#==========================================================================================

# Approach 4: List + Pointer with Boundary Trick (Optimal)
# - Same as Approach 1 but instead of truncating, just track a rightBound variable
# - visit(url): increment current, overwrite or append, set rightBound = current
# - back(steps): current = max(0, current - steps)
# - forward(steps): current = min(rightBound, current + steps)
# Time Complexity: ALL operations O(1)
# Space Complexity: O(n)
# No slicing, no traversal — pure index math


#==========================================================================================
#Approach 1: List + Truncate (Array-based) — Most Intuitive
#Time Complexity: visit O(n) worst case due to list slicing, back/forward O(1)
#Space Complexity: O(n)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.track = [homepage]
        self.curr_ptr = len(self.track)-1

    def visit(self, url: str) -> None:
        #At every visit, clear the forward history
        self.track = self.track[:self.curr_ptr+1]
        self.curr_ptr += 1
        self.track.insert(self.curr_ptr,url)
        
        
    def back(self, steps: int) -> str:
        #Doing clamping so that it does not go out of bounds
        self.curr_ptr = max(0,self.curr_ptr - steps) #clamp to 0
        return self.track[self.curr_ptr]

    def forward(self, steps: int) -> str:
        #Doing clamping so that it does not go out of bounds
        self.curr_ptr = min(len(self.track)-1,self.curr_ptr + steps) # clamp to last index
        return self.track[self.curr_ptr]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

#==========================================================================================
#Approach 4: List + Pointer with Boundary Trick (Optimal)
#Time Complexity: O(1)
#Space Complexity: O(n)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.track = [homepage]
        self.curr_ptr = len(self.track)-1
        self.bound  = 0

    def visit(self, url: str) -> None:
        self.curr_ptr += 1
        if self.curr_ptr < len(self.track):
            self.track[self.curr_ptr] = url  # overwrite instead of slice
        else:
            #if there is no extra space
            #we just add it 
            self.track.append(url)
        #now update the bound of the list
        self.bound = self.curr_ptr

        
    def back(self, steps: int) -> str:
        self.curr_ptr = max(0,self.curr_ptr - steps) #clamp to 0
        return self.track[self.curr_ptr]

    def forward(self, steps: int) -> str:
        #we work on the boundary rather than len of the list
        #correctly marks the end of valid history
        self.curr_ptr = min(self.bound,self.curr_ptr + steps) # clamp to last index
        return self.track[self.curr_ptr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)