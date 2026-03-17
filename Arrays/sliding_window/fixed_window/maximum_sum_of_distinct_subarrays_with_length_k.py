from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        max_sum = 0
        curr_sum = 0
        longest_substring = {}
        while(j < len(nums)):
            if nums[j] not in longest_substring:
                longest_substring[nums[j]] = 0
            longest_substring[nums[j]] += 1
            curr_sum += nums[j]
            if ((j-i+1) < k):
                j += 1
            elif ((j-i+1) == k):
                if len(longest_substring) == k:
                    max_sum = max(max_sum, curr_sum)
                longest_substring[nums[i]] -= 1
                if longest_substring[nums[i]] == 0:
                    del longest_substring[nums[i]]
                curr_sum -= nums[i]
                i += 1
                j += 1

        return max_sum

        