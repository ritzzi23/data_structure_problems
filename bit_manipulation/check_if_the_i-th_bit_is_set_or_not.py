#https://chatgpt.com/share/6873139c-73a8-800c-9e9e-c9b33aa5248d


#check_if_the_i-th_bit_is_set_or_not.py
#time complexity: O(1)
#space complexity: O(1)
class Solution:
    def checkKthBit(self, n, k):
        mask = 1<<k
        if n & mask:
            return True 
        return False
