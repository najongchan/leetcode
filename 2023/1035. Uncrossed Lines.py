# https://leetcode.com/problems/uncrossed-lines/
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        return table[m][n]


x = Solution()
print(x.maxUncrossedLines([1, 4, 2], [1, 2, 4]))  # 2
print(x.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))  # 3
print(x.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))  # 2
