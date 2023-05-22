# https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan-v2&id=dynamic-programming
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return min(dp[n-1], dp[n-2])


x = Solution()
print(x.minCostClimbingStairs([10, 15, 20]))
