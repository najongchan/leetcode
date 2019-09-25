# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: [int]) -> int:
        max_area = 0
        left_point = 0
        right_point = len(height) - 1

        while left_point < right_point:
            area = (right_point - left_point) * min(height[left_point], height[right_point])
            max_area = max(area, max_area)
            if height[left_point] < height[right_point]:
                left_point += 1
            else:
                right_point -= 1

        return max_area


        # brute force
        #
        # max_area = 0
        # x_axis = len(height)

        # for i in range(x_axis):
        #     for j in range(i, x_axis):
        #         if i == j:
        #             continue
                
        #         area = abs(i-j) * min(height[i], height[j])
        #         max_area = max(area, max_area)
        # return max_area

input = [1,8,6,2,5,4,8,3,7]
temp = Solution()
print(temp.maxArea(input))