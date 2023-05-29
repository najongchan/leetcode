# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count = 1
            else:
                count += 1
            if count > (len(nums)/2):
                return nums[i]
        return nums[-1]