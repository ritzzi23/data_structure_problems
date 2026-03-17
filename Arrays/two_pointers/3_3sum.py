#Time complexity: O(n^2)
#Space complexity: O(1)
from typing import List
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = []
        for i in range(len(nums)):
            # Skip duplicates for the first number
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1  # Two pointers
            
            while(j<k):
                current_sum = nums[i] + nums[j] + nums[k]
                if(current_sum < 0):
                    j += 1
                elif(current_sum > 0):
                    k -= 1
                else:
                    d.append([nums[i], nums[j], nums[k]])
                    #after finding the triplet, we need to skip the duplicates for the second and third numbers
                    # Skip duplicates for the second number
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # Skip duplicates for the third number
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return d
