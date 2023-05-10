# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        for i in range(1, len(nums)):
            if nums[cur] != nums[i]:
                cur += 1
                nums[cur] = nums[i]

        return cur + 1


