'''
    Approach	Time	Space	Idea
Brute Force	O(n²)	O(1)	For each position, scan left and right to find max walls
Prefix/Suffix Arrays	O(n)	O(n)	Pre-compute max left & max right arrays
Two Pointers	O(n)	O(1)	Move inward from both ends
Monotonic Stack	O(n)	O(n)	Find boundaries using a stack
    ''' 