# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return index