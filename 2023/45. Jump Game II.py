# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_jump, count, next_position = 0, 0, 0

        for i in range(len(nums) - 1):
            count += 1
            max_jump = max(max_jump, i + nums[i])

            if i == next_position:
                next_position = max_jump
            if max_jump >= len(nums) - 1:
                return count
        return count