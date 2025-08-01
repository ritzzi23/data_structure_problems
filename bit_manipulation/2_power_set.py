#Iterative solution
#time complexity: O(2^n)
#space complexity: O(1) for result storage
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])
            result.extend(new_subsets)
        return result
#-------------------------------------------------------------------------------------------
#Recursive solution
#time complexity: O(2^n)
#space complexity: O(n) for recursion stack
#https://chatgpt.com/share/687309d8-8aec-800c-bf13-549bf8b49363
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        # Get subsets without first element
        subsets_without_first = self.subsets(nums[1:])
        # Get subsets with first element
        subsets_with_first = []
        for subset in subsets_without_first:
            subsets_with_first.append([nums[0]] + subset)

        return subsets_without_first + subsets_with_first
#-------------------------------------------------------------------------------------------
#Bit Manipulation solution
#time complexity: O(n * 2^n)
#space complexity: O(n * 2^n) for result storage
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = 1 << len(nums)  # 2^len(nums)
        result = []
        for num in range(n):
            subset = []
            for j in range(len(nums)):
                if num & (1<<j):
                    subset.append(nums[j])
            result.append(subset)
        return result


         
        