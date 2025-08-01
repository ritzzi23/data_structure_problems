#time complexity: O(log n)
#space complexity: O(1)
from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
        #base case
        if x < 2:
            return x
        
        low = 1
        high = x // 2 
        # We can safely use x // 2 because the square root of any number 
        # greater than 1 is always less than or equal to half of that number.

        result = 0
        # equal to condition is used to handle perfect squares
        while(low<=high):
            mid = low +(high-low)//2
            
            check = (mid*mid)
            if check == x:
                return mid 
                
            elif check > x:
                high = mid-1
            else:
                result = mid
                low = mid+1
        return result
        