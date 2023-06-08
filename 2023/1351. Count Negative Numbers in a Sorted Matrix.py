# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
from typing import List


class Solution:
    def binarySearch(self, row):
        start, end = 0, len(row)
        while start < end:
            mid = start + (end - start) // 2
            if row[mid] < 0:
                end = mid
            else:
                start = mid + 1

        return len(row) - start

    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        for row in grid:
            answer += self.binarySearch(row)
        return answer


x = Solution()
print(x.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
