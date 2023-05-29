# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())