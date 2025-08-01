#Meet in the Middle Solution
'''
Split the array into two halves:
    left = nums[:n//2]
    right = nums[n//2:]
Generate all subset sums of left and right using bitmasking.
Sort the subset sums of right.
For each sum s in the subset sums of left:
    Calculate required = target - s where target = sum(nums)//2.
    Use binary search on sorted right sums to check if required exists.
If any required is found in right sums, return True.
If no match found after checking all, return False''' 


#time complexity: O(n * 2^n) for generating subset sums
#space complexity: O(n * 2^n) for storing subset sums
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        total //= 2
        #Step 1: Split the array into two halves
        left = nums[:n // 2]
        right = nums[n // 2:]

        #Step 2: Generate all subset sums of left and right
        def get_subset_sums(arr):
            n = 1 << len(nums)  # 2^len(nums)
            result = []
            for num in range(n):
                subset_sum = 0
                for j in range(len(arr)):
                    if num & (1 << j):
                        subset_sum += arr[j]
                result.append(subset_sum)
            return result
        
        left_sums = get_subset_sums(left)
        right_sums = get_subset_sums(right)
        #Step 3: Sort the subset sums of right
        right_sums.sort()

        #Step 4: Check for each sum in left if the required sum exists in right
        def binary_search(arr, target):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        #Step 5: Check if any required sum exists
        for s in left_sums:
            required = total - s
            if binary_search(right_sums, required):
                return True
        return False
#-------------------------------------------------------------------------------------------
#time complexity: O(n * 2^n) for generating subset sums
#space complexity: O(n * 2^n) for storing subset sums using combinations
from typing import List
from itertools import combinations

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        n = len(nums)
        left = nums[:n//2]
        right = nums[n//2:]

        def get_all_sums(arr):
            sums = []
            for r in range(len(arr) + 1):
                for comb in combinations(arr, r):
                    sums.append(sum(comb))
            return sums

        left_sums = get_all_sums(left)
        right_sums = get_all_sums(right)
        right_sums_set = set(right_sums)

        for s in left_sums:
            if target - s in right_sums_set:
                return True

        return False
#-------------------------------------------------------------------------------------------
#time complexity: O(n * 2^n) for generating subset sums
#space complexity: O(n * 2^n) for storing subset sums using binary search
from typing import List
import bisect

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        n = len(nums)
        left = nums[:n//2]
        right = nums[n//2:]

        def get_subset_sums(arr: List[int]) -> List[int]:
            n = 1 << len(arr)
            result = []
            for num in range(n):
                subset_sum = 0
                for j in range(len(arr)):
                    if num & (1 << j):
                        subset_sum += arr[j]
                result.append(subset_sum)
            return result

        left_sums = get_subset_sums(left)
        right_sums = get_subset_sums(right)
        right_sums.sort()  # For binary search

        for s in left_sums:
            required = target - s
            idx = bisect.bisect_left(right_sums, required)
            if idx < len(right_sums) and right_sums[idx] == required:
                return True

        return False
#-------------------------------------------------------------------------------------------
