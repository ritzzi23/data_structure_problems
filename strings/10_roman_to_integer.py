#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n = len(s)
        result = 0
        for i in range(n):
            curr_val = roman_map[s[i]]

            if i+1 < n:
                next_val = roman_map[s[i+1]]
                if curr_val< next_val:
                    result -= curr_val
                else:
                    result += curr_val
            else:
                result += curr_val
        return result
#---------------------------------------------------------------------------
    