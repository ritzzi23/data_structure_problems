'''
Your understanding in clean form
expand the window until it becomes valid
once it is valid:
record its length as a candidate answer
shrink from the left
check if it is still valid
if yes, record again
keep shrinking until it becomes invalid

So in one valid phase, you are trying to find:

the smallest valid window for that current end
'''



#My Version of the solution
#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        min_length = float('inf')
        current_sum = 0     
        while (end < len(nums)): #Time Complexity: O(n)
            #calculations 
            current_sum += nums[end]

            if (current_sum < target):
                #opertation
                end += 1

            elif (current_sum == target):
                #opertation
                while current_sum >= target: #Time Complexity: O(n) (but amortized because start pointer moves only forward)
                    min_length = min(min_length,(end-start+1))
                    current_sum -= nums[start]
                    start += 1
                end += 1 

            elif (current_sum > target):
                while current_sum >= target:
                    min_length = min(min_length,(end-start+1))
                    current_sum -= nums[start]
                    start += 1
                end += 1

        return 0 if min_length == float('inf') else min_length


    







        