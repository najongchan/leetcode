# https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&id=dynamic-programming
from typing import List
import math


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_square = 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    max_square = max(dp[i][j], max_square)

        return max_square ** 2


x = Solution()
print(x.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(x.maximalSquare([["0", "1"], ["1", "0"]]))
print(x.maximalSquare([["0"]]))
