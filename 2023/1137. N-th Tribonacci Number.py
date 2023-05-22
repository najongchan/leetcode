# https://leetcode.com/problems/n-th-tribonacci-number/?envType=study-plan-v2&id=dynamic-programming
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1] + dp[i - 3]
        return dp[n]
