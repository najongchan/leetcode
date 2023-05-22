# https://leetcode.com/problems/delete-and-earn/?envType=study-plan-v2&id=dynamic-programming
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 1)

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in range(1, max(nums) + 1):
            dp[num] = max(dp[num - 1], dp[num - 2] + num * freq.get(num, 0))
        return dp[-1]


x = Solution()
print(x.deleteAndEarn([2, 2, 3, 3, 3, 4]))
print(x.deleteAndEarn([3,4,2]))
