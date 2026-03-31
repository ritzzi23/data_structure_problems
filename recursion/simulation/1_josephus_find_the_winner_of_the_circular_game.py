'''
Approaches
**Simulation with List

Maintain a list of players, repeatedly remove the k-th person
Use modular arithmetic to wrap around: index = (index + k - 1) % len(list)
Time: O(n^2) due to list removals, Space: O(n)

**Simulation with Queue (deque)

Rotate the deque k-1 times (move front to back), then pop the front
Repeat until one player remains
Time: O(n*k), Space: O(n)

**Josephus Formula (Iterative)

Classic math recurrence: J(1) = 0, J(n) = (J(n-1) + k) % n
Build up from base case in a loop, return result + 1 (1-indexed)
Time: O(n), Space: O(1) — optimal

**Josephus Formula (Recursive)

Same recurrence but solved recursively
josephus(1) = 0, josephus(n) = (josephus(n-1) + k) % n
Time: O(n), Space: O(n) call stack
Simulation with Circular Linked List

Build a circular linked list, walk k-1 steps and remove the next node
Repeat until one node points to itself
Time: O(n*k), Space: O(n)
'''


#Simulation with List

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        arr = []
        for elem in range(1,n+1):
            arr.append(elem)
        while len(arr) > 1:
            i = (i + k - 1) % len(arr)
            arr.pop(i)
        return arr[0]

#---------------------------------------------------------------------------------------------------------------

#Simulation with Queue (deque)

'''
Time: O(n * k)

The while loop runs n - 1 times (one elimination per round)
Each round does k - 1 rotations inside the for loop
Total operations: (n-1) * (k-1) ≈ O(n * k)
Space: O(n)

The deque holds all n players initially
'''

'''
How to remember this

Imagine people are standing in a line that loops:

take front person and send to back
do this k-1 times
now the k-th person is at front
remove them

Repeat.
'''

from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        arr = deque()
        for elem in range(1,n+1):
            arr.append(elem)
        while len(arr) > 1:
            for _ in range(k-1):
                arr.append(arr.popleft())
            arr.popleft()
        return arr[0]


#---------------------------------------------------------------------------------------------------------------

#Josephus Formula (Iterative)


