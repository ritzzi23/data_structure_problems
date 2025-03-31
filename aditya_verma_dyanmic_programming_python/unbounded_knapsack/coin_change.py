"""maximum number of ways to make a given amount using the given coins 
(instead of the minimum number of coins), you need to use a variation of the Coin Change
 problem that counts the number of ways to achieve the amount."""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]


        pass