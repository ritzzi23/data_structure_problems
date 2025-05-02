#The upper bound is the first position where a number greater than the target can be inserted.

#If the target exists, it points to the position after the last occurrence of the target.

#If the target doesn’t exist, it points to the position where the target would be 
# inserted after all elements smaller or equal to it.

#"Where can I place a number strictly larger than the target?"

#User function Template for python3
class Solution:
    def upperBound(self, arr, target):
        #code here
        low = 0
        high = len(arr) -1
        result = len(arr)
        while (low <= high):
            mid = int(low + (high-low)//2)
            if arr[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result


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
        ans = ob.upperBound(A, D)
        print(ans)
        print("~")

# } Driver Code Ends