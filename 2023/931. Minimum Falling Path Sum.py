# https://leetcode.com/problems/minimum-falling-path-sum/?envType=study-plan-v2&id=dynamic-programming
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += min(matrix[i - 1][j - (j > 0):j + 1 + (j < n)])
        return min(matrix[-1])


x = Solution()
print(x.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(x.minFallingPathSum([[-19, 57], [-40, -5]]))
