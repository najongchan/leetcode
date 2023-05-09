# https://leetcode.com/problems/find-the-difference-of-two-arrays/\
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1).difference(nums2)), list(set(nums2).difference(nums1))]


x = Solution()
print(x.findDifference([1, 2, 3], [2, 4, 6]))  # [[1,3],[4,6]]
print(x.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))  # [[1,3],[4,6]]
