#time complexity: O(log n)
#the search space is halved at each step, leading to logarithmic time complexity.
#binary search is efficient for sorted arrays, making it suitable for this problem.
#space complexity: O(1)
#the space complexity is O(1) because we are not using any extra space that grows with input size.
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while(low<=high): 
            mid = int(low + (high-low)//2)
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return -1

#-------------------------------------------------------
#Pure Recursive Solution
# time complexity: O(log n)
# space complexity: O(log n) for recursion stack
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, low, high):
            if low > high:
                return -1
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(nums, target, low, mid - 1)
            else:
                return binary_search(nums, target, mid + 1, high)
        
        return binary_search(nums, target, 0, len(nums) - 1)
#-------------------------------------------------------
        