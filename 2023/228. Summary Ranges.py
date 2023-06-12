# https://leetcode.com/problems/summary-ranges/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        left, right = 0, 0

        while right < len(nums) - 1:
            if nums[right] + 1 == nums[right + 1]:
                right += 1
            else:
                if right == left:
                    result.append(str(nums[right]))
                else:
                    result.append(str(nums[left]) + "->" + str(nums[right]))
                right += 1
                left = right

        if right == left:
            result.append(str(nums[right]))
        else:
            result.append(str(nums[left]) + "->" + str(nums[right]))
        return result

x = Solution()
print(x.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(x.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(x.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
