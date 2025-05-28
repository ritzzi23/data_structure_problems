'''Given an array arr[] which represents dimensions of sequence of 
matrices where the ith matrix has the dimensions (arr[i-1] x arr[i]) for i>=1.,
find the most efficient way to multiply these matrices together.
The efficient way is the one that involves the least number of multiplications.'''

class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        def helper(i,j):
            if(i>=j):
                return 0
            min_value = float('inf')
            for k in range(i,j):
                temp_min = (helper(i,k) 
                            + helper(k+1, j)
                            + (arr[i-1] * arr[k] * arr[j]))
                min_value = min(min_value,temp_min)
            return min_value
        return helper(1,n-1)
    
arr = [2, 1, 3, 4]
a = Solution()
print(a.matrixMultiplication(arr))