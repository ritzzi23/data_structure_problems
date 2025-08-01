#Iterative solution
#time complexity: O(log n)
#space complexity: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True
#-------------------------------------------------------------------------------------------
#Recursive solution
#time complexity: O(log n)
#space complexity: O(log n) for recursion stack
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)
#-------------------------------------------------------------------------------------------
#Bit Manipulation solution
#time complexity: O(1)
#space complexity: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0