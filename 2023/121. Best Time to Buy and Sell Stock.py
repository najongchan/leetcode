# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            if cur_profit > 0:
                max_profit = max(max_profit, cur_profit)
            else:
                left = right

            right += 1
        return max_profit