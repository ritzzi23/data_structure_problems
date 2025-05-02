#The lower bound of a target in a sorted array is the first 
# position where the target could be inserted without breaking the sort order.
#If the target exists, it points to the first occurrence of the target.
#If the target doesn’t exist, it points to the position of the smallest number greater than or equal to the target.



#User function Template for python3
class Solution:
    def lowerBound(self, arr, target):
        #code here
        low = 0
        high = len(arr) -1
        result = len(arr)
        while (low <= high):
            mid = int(low + (high-low)//2)
            if arr[mid] >= target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result
    
nums = [0,1,7,4,4,5]
lower = 3
a = Solution()
print(a.lowerBound(nums,lower))        

'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.lowerBound(A, D)
        print(ans)
        print("~")

# } Driver Code Ends'''