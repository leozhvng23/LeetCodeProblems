"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dynamic programming
        # O(S*n)
        """
        opt = [float('inf')] * (amount + 1)
        opt[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c and opt[i-c] != float('inf'):
                        opt[i] = min(opt[i], opt[i-c] + 1)

        return opt[amount] if opt[amount] != float('inf') else -1
        """
        opt = [float("inf")] * (amount + 1)
        opt[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                opt[x] = min(opt[x], opt[x - coin] + 1)

        return opt[amount] if opt[amount] != float("inf") else -1
