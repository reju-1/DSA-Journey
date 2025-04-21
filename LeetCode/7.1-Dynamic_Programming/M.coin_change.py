"""
322. Coin Change
links: https://leetcode.com/problems/coin-change/
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Time: O()
        Space: O()
        """
        memo = {}

        def helper(remain_amount):
            if remain_amount == 0:
                return 0

            if remain_amount in memo:
                return memo[remain_amount]

            result = float("inf")
            for coin in coins:
                if coin <= remain_amount:
                    count = 1 + helper(remain_amount - coin)
                    result = min(result, count)

            memo[remain_amount] = result

            return result

        result = helper(amount)
        return result if result != float("inf") else -1
