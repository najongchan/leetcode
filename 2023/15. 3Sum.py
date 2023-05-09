# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        combi = set()

        for n in range(len(nums)):
            i = n + 1
            j = len(nums) - 1

            while i < j:
                summ = nums[n] + nums[i] + nums[j]
                if summ == 0:
                    combi.add((nums[n], nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif summ > 0:
                    j -= 1
                elif summ < 0:
                    i += 1
        for i in combi:
            answer.append(list(i))

        return answer



x = Solution()
print(x.threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(x.threeSum([0,1,1]))  # []
print(x.threeSum([0,0,0]))  # [[0,0,0]]