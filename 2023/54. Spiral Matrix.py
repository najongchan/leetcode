# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1 <= m, n <= 10
        # -100 <= matrix[i][j] <= 100
        m, n = len(matrix), len(matrix[0])
        vector = 1
        answer = []

        while len(answer) < m * n:
            if vector > 0:
                answer += matrix.pop(0)
                for i in range(0, len(matrix), vector):
                    answer.append(matrix[i].pop())
            else:
                answer += reversed(matrix.pop())
                for i in range(len(matrix) - 1, -1, vector):
                    answer.append(matrix[i].pop(0))
            vector *= -1
        return answer


x = Solution()
print(x.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
print(x.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
print(x.spiralOrder(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))  # [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
