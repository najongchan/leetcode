# https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&id=dynamic-programming
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0] * (n+1) for _ in range(m+1)]
        grid[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                grid[i][j] += grid[i-1][j] + grid[i][j-1]

        return grid[m][n]


x = Solution()
print(x.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(x.uniquePathsWithObstacles([[0,1],[0,0]]))