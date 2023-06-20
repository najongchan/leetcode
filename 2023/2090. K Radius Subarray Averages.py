# https://leetcode.com/problems/k-radius-subarray-averages/
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        if k * 2 + 1 > n:
            return result

        left = 0
        cur_sum = sum(nums[:2 * k + 1])
        length = k * 2 + 1

        result[left + k] = cur_sum // length

        for right in range(2 * k + 1, n):
            cur_sum -= nums[left]
            left += 1
            cur_sum += nums[right]
            result[left + k] = cur_sum // length

        return result
