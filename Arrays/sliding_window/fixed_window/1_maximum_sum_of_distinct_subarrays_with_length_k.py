#Brute Force
#time Complexity : Time Complexity: O(n * k)
#space Complexity : O(k)
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0 #Space Complexity: O(1)
        for i in range(len(nums)): #Time Complexity: O(n)
            curr_sum = 0
            j = i + k
            if j<= len(nums):
                if len(set(nums[i:j])) == k: #Time Complexity: O(k)
                    curr_sum = sum(nums[i:j]) #Time Complexity: O(k)
            else:
                break
            max_sum = max(max_sum, curr_sum)
            
        return max_sum

#-----------------------------------------------------------------------------------

#Optimal Solution
#time Complexity : Time Complexity: O(n)
#space Complexity : O(k)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        total_max = 0
        curr_sum = 0
        n = len(nums)
        freq = {} #Space Complexity: O(k)   
        #make sure your window size end not goes beyond size of the list
        while (end < n): #Time Complexity: O(n)
            #we do the basic computation here 
            if nums[end] not in freq:
                freq[nums[end]] = 0
            freq[nums[end]] += 1
            curr_sum += nums[end]
            # let's make the window size (fixed window size)
            if (end - start + 1) < k:
                end += 1
            #once we reach the window size
            elif (end - start + 1) == k:
                #now we need to maintain the window size
                #do the computation 
                if len(freq) == k:
                    total_max = max(total_max, curr_sum) #Time Complexity: O(1)
                freq[nums[start]] -= 1  
                #because it may go negative so on zero we remove that element 
                if freq[nums[start]] == 0:
                    del freq[nums[start]] #Time Complexity: O(1)
                curr_sum -= nums[start]
                #Slide the window 
                start += 1
                end += 1
        return total_max