"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if len(prices) == 0 or len(prices) == 1:
            return max_profit

        p1 = 0  # left
        p2 = 1  # right

        while p2 < len(prices):
            if prices[p2] <= prices[p1]:
                # reset the pointers, as right is less than left
                p1 = p2

            else:
                # calculate profit as right is bigger than left
                max_profit = max(prices[p2] - prices[p1], max_profit)

            p2 = p2 + 1

        return max_profit
