# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= n:
                print(i, nums[i], n)
                n = i
        return n == 0