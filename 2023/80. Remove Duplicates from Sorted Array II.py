# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        for num in nums:
            if cur < 2 or num != nums[cur-2]:
                nums[cur] = num
                cur += 1
        return cur


x = Solution()
print(x.removeDuplicates([1]))
print(x.removeDuplicates([1, 2]))
print(x.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(x.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
