# https://leetcode.com/problems/spiral-matrix-ii/
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 1

        top, right, down, left = 0, n-1, n-1, 0

        while count < n**2 + 1:
            for i in range(left, right + 1):
                matrix[top][i] = count
                count += 1
            top += 1

            for i in range(top, down + 1):
                matrix[i][right] = count
                count += 1
            right -= 1

            for i in range(right, left - 1, -1):
                matrix[down][i] = count
                count += 1
            down -= 1

            for i in range(down, top - 1, -1):
                matrix[i][left] = count
                count += 1
            left += 1

        return matrix


x = Solution()
print(x.generateMatrix(3))  # [[1,2,3],[8,9,4],[7,6,5]]