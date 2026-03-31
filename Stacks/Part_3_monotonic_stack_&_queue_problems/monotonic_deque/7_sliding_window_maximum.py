from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        #to make it monotonic 
        # Walk through every number in nums, left to right
        for i in range(len(nums)):
            #we work with indices 
            #we have to do 2 things here 
            #We always keep the max value elem (indice) in front of deque
            #Second is that we have to elimnate the index that is not part of the current window

            #remove expired index from front because Oldest element exist in front (queue FIFO)
            #remove smaller values from back

            # remove indices outside the current window 
            while dq and dq[0] <= (i-k):
                dq.popleft() 
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            #we keep appending till we reach the first valid window
            dq.append(i)
            #first window is formed when i = k-1
            #and after that all the windows are valid 
            if i>=k-1:
                result.append(nums[dq[0]])
        return result
            
                 
