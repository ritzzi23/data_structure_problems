from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum = sum(nums)
        if list_sum%2!=0:
            return False 
        else:
            subset_sum = list_sum//2
            n = len(nums)
            dp = [[False] * (subset_sum + 1) for _ in range(n+1)]
            for k in range(n+1):
                dp[k][0] = True
            for i in range(1,n+1):
                for j in range(1,subset_sum+1):
                    if(nums[i-1]<= j):
                        dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[n][subset_sum] if dp[n][subset_sum] else False
a = Solution()
nums = [1,5,11,5]
print(a.canPartition(nums))

