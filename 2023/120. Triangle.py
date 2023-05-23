# https://leetcode.com/problems/triangle/?envType=study-plan-v2&id=dynamic-programming
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # triangle[i][j] += min(triangle[i-1][j-(j==i)],  # minimum sum from coordinate (x-1, y)
                #                       triangle[i-1][j-(j>0)])   # minimum sum from coordinate (x-1, y-1)
                if 0 < j != i:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                else:
                    if j == 0:
                        triangle[i][j] += triangle[i-1][j]
                    else:
                        triangle[i][j] += triangle[i-1][j-1]

        return min(triangle[-1])


x = Solution()
print(x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
