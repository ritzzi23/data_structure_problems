#Without Inplace Modification
#Using Additional Space

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        result = []
        i = 0
        j = 1
        current_count = 1
        while j < len(chars):
            if chars[i] != chars[j]:
                result.append(chars[i])
                if current_count > 1:
                    for digit in str(current_count):
                        result.append(digit)
                i = j
                j += 1
                current_count = 1
            else:
                current_count += 1
                j += 1

        result.append(chars[i]) 
        if current_count > 1:
            for digit in str(current_count):
                result.append(digit)  

        return len(result)

#----------------------------------------------------------

#With Inplace Modification

'''
Time Complexity: O(n)
The while loop iterates through each character exactly once (j increments every iteration), 
so it's a single pass through the array.
The inner for digit in str(current_count) loop converts the count to digits, 
but the total digits written across the entire execution is bounded by O(n), 
so it doesn't add an extra factor.
'''

'''
Space Complexity: O(1)
The compression is done in-place — no extra array is allocated.
Only a few integer variables (i, j, current_count) are used.
str(current_count) creates a small temporary string, 
but its size is at most O(log n) digits, 
which is effectively constant for practical inputs.
'''



class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        i = 0
        j = 0
        current_count = 1
        while j < len(chars):
            if j == len(chars) - 1 or chars[j] != chars[j+1]:
                chars[i] = chars[j]
                i += 1
                if current_count > 1:
                    for digit in str(current_count):
                        chars[i] = digit
                        i += 1
                j += 1
                current_count = 1
            else:
                current_count += 1
                j += 1

        return i
        
        