#Meet in the Middle Solution
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)// 2

        #Step 1: Split the array into two halves
        left = nums[:n]
        right = nums[n:]

        #Step 2: Generate all possible subset sums for both halves
        def generate_subset_sums(arr):
            n = 1 << len(arr)
            subset_sums = []
            for i in range(n):
                total = 0
                for j in range(len(arr)):
                    if i & (1 << j):
                        total += arr[j]
                subset_sums.append(total)
            return subset_sums
        

        left_sums = generate_subset_sums(left)
        right_sums = generate_subset_sums(right)

        #Step 3: Sort the right subset sums for binary search
        right_sums.sort()

        #Step 4: Find the minimum difference
        min_diff = abs(sum(left) - sum(right))
        total_sum = sum(nums)
        target = total_sum // 2

        #Step 5: Define binary search function with right bound
        def bisect_right(arr, target):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        #Step 6: Iterate through left subset sums and find the closest right subset sum
        for left_sum in left_sums:
            # Calculate the target for the right subset
            target_right = target - left_sum
            
            # Find the index of the smallest right sum that is greater than target_right
            idx = bisect_right(right_sums, target_right)
            
            # Check the closest right sum and calculate the difference
            if idx < len(right_sums):
                right_sum = right_sums[idx]
                min_diff = min(min_diff, abs(total_sum - 2 * (left_sum + right_sum)))
            if idx > 0:
                right_sum = right_sums[idx - 1]
                min_diff = min(min_diff, abs(total_sum - 2 * (left_sum + right_sum)))
        return min_diff
    
    


    


