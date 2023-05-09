# https://leetcode.com/problems/matchsticks-to-square/

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False

        sum_of_nums = sum(nums)
        if sum_of_nums % 4 != 0:
            return False

        side_length = int(sum_of_nums / 4)
        sides = [side_length] * 4
        nums.sort(reverse=True)
        # print(nums)

        def dfs(nums, index, sides):
            if index == len(nums):
                return True

            for i in range(4):
                if sides[i] >= nums[index]:
                    sides[i] -= nums[index]
                    if dfs(nums, index+1, sides):
                        return True
                    sides[i] += nums[index]
            return False

        return dfs(nums, 0, sides)
