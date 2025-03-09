"""
121. Best Time to Buy and Sell Stock
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Buy low sell hight
        """

        max_profit = 0
        min_price = prices[0]

        for curr_price in prices:
            if curr_price < min_price:
                min_price = curr_price

            profit = curr_price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

    def maxProfit(self, prices: list[int]) -> int:
        """
        Technique: Two pointers
        Buy low sell high
        """

        i, j = 0, 1
        max_profit = 0

        while j < len(prices):
            diff = prices[j] - prices[i]
            max_profit = max(max_profit, diff)

            if diff < 0:
                i = j
            j += 1

        return max_profit
