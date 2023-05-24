# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        index_one, index_two = 0, 0
        while index_two < n and index_one < m + n:
            if nums1[index_one] >= nums2[index_two]:
                nums1.insert(index_one, nums2[index_two])
                nums1.pop()
                index_two += 1
            else:
                index_one += 1

        count = n - index_two
        while count > 0:
            nums1.pop()
            count -= 1
        nums1 += nums2[index_two:]


x = Solution()
print(x.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(x.merge([-1, -1, 0, 0, 0, 0], 4, [-1, 0], 2))
print(x.merge([-1, 3, 0, 0, 0, 0, 0], 2, [0, 0, 1, 2, 3], 5))
