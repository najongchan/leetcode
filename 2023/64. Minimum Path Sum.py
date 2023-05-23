# https://leetcode.com/problems/minimum-path-sum/?envType=study-plan-v2&id=dynamic-programming
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i > 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]

        return grid[m-1][n-1]

x = Solution()
print(x.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
