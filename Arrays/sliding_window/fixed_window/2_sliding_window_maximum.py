#Brute Force
#Time Complexity: O(n*k)
#Space Complexity: O(1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        result = []
        while (end < len(nums)): #Time Complexity: O(n)
            #calculation

            if (end - start + 1) < k:
                end += 1
            
            elif (end - start + 1) == k:
                nums_1 = nums[start:end+1] #Time Complexity: O(k)
                result.append(max(nums_1)) #Time Complexity: O(k)
                start += 1
                end += 1
        return result

#-----------------------------------------------------------------------------------

#we don't use len of heap here because it will be very difficult to remove the element which is out of window
#Optimal Solution
#Time Complexity: O(n)
#Space Complexity: O(k)
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        result = []
        #We will maintain a max heap of size k to get immediate access to max element
        heap = [] #Space Complexity: O(k)
        for i in range(len(nums)): #Time Complexity: O(n)

            #push the element in heap and also keep track of index so that we can remove the element which is out of window
            heapq.heappush(heap,(-nums[i],i)) #Time Complexity: O(log k)

            #as the max heap will give the max element alsways
            #We need to check two things 
            #First that the window is formed or not 
            #and if the window is formed then check that the max element is not out of the window
            #if the max element is out of the window then remove it from the heap
            #for an element to stay in the window its index should be greater than or equal to (i-k+1)
            while heap and heap[0][1] <= (i-k): #Time Complexity: O(log k)
                heapq.heappop(heap) 

            #first window is formed when i = k-1
            #and after that all the windows are valid 
            if i >= k-1:
                #the max element is at the top of the heap
                result.append(-heap[0][0])
        return result

#-----------------------------------------------------------------------------------
#Best Solution
#Monotonic Deque


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() #Space Complexity: O(k)
        result = [] #Space Complexity: O(n-k+1)
        #to make it monotonic 
        # Walk through every number in nums, left to right
        for i in range(len(nums)): #Time Complexity: O(n)
            #we work with indices 
            #we have to do 2 things here 
            #We always keep the max value elem (indice) in front of deque
            #Second is that we have to elimnate the index that is not part of the current window

            #remove expired index from front because Oldest element exist in front (queue FIFO)
            #remove smaller values from back

            # remove indices outside the current window 
            while dq and dq[0] <= (i-k): #Time complexity: O(1)
                dq.popleft() 
            
            #Always remove smaller values from back because we are appending from back and 
            #if the current element is greater than the last element then the last element is useless
            #because it can never be the maximum element in any future window
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            #we keep appending till we reach the first valid window
            dq.append(i)
            #first window is formed when i = k-1
            #and after that all the windows are valid 
            if i>=k-1:
                result.append(nums[dq[0]])
        return result
            
                 
