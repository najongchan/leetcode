# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            cur_profit = prices[right] - prices[left]
            if cur_profit > 0:
                max_profit += cur_profit
            left = right
        return max_profit