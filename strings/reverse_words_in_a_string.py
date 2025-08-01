#Manual solution without using any library functions
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        final_string = ''
        for j in range(len(a)-1,-1,-1):
            result_string = "".join(a[j])
            final_string += result_string
            if j>0:
                 final_string += " "
            
        return(final_string)
#------------------------------------------------------------------------------------------------
#Optomal solution
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a.reverse()
        return (" ".join(a))
#-----------------------------------------------------------------------------------------
        
