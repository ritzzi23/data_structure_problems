'''
Time: O(n) where n is the number of digits in x. 
The for loop, [::-1], and ''.join() each iterate over the digits.

Space: O(n). The result list and the joined string both store n characters.
'''

#String Reversal Method
class Solution:
    def reverse(self, x: int) -> int:
        result = []
        if x<0:
            sign = '-'
        else:
            sign = ''
        x = abs(x)
        for i in str(x):
            result.append(i)

        result = result[::-1]
        final = int(sign + ''.join(result))
        if final > ((2**31) -1) or final < (-(2**31)):
            return 0
        else:
            return final

#---------------------------------------------------------------------
'''
Time: O(n) where n is the number of digits. 
The while loop runs once per digit.

Space: O(1). 
Only a fixed number of variables (sign, final, remainder) regardless of input size.
'''


#Mathematical Method

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        final = 0
        while x!= 0:
            remainder = x%10
            x = x//10
            final = final * 10 + remainder

        final *= sign

        if final > ((2**31) -1) or final < (-(2**31)):
            return 0
        return final