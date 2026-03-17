
#Brute_force:
#Time complexity: O(n^2)
#Space complexity: O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # Return an empty list if no solution is found
        return []  

#----------------------------------------------------

# Dictionary_Approach:
# Time complexity: O(n)
# Space complexity: O(n)
from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_maps = defaultdict()
        #elem as key and index as value
        for index, elem in enumerate(nums):
            remaining = target - elem 

            if remaining in nums_maps:
                return nums_maps[remaining], index
            nums_maps[elem] = index
        return []

#----------------------------------------------------

# Two_pointer_Approach:
# Time complexity: O(n log n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a list of tuples containing the index and the element
        num_index_list = [(index, elem) for index, elem in enumerate(nums)]
        # Sort the list by the element
        num_index_list.sort(key=lambda x: x[1])
        left = 0
        right = len(nums) - 1

        while(left != right):
            # Calculate the sum of the two elements from the sorted list
            current_sum = num_index_list[left][1] + num_index_list[right][1]
            if current_sum < target:
                # If the sum is less than the target, move the left pointer to the right
                left += 1
            elif current_sum > target:
                # If the sum is greater than the target, move the right pointer to the left
                right -= 1
            else:
                # If the sum is equal to the target, return the indices of the two elements
                return num_index_list[left][0], num_index_list[right][0]

