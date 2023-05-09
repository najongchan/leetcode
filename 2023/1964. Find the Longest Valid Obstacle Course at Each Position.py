# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        lis = []
        ans = []
        for i in range(n):
            # 이진 탐색으로 현재 장애물을 마지막으로 하는 최대 코스의 길이를 찾음
            from bisect import bisect_left
            pos = bisect_left(lis, obstacles[i])
            ans.append(pos+1)

            # 이진 탐색으로 lis 배열에 현재 장애물의 높이를 삽입
            if not lis or obstacles[i] >= lis[-1]:
                lis.append(obstacles[i])
            else:
                lis[pos] = obstacles[i]

        return ans


x = Solution()
print(x.longestObstacleCourseAtEachPosition([1, 2, 3, 2]))  # [1,2,3,3]
print(x.longestObstacleCourseAtEachPosition([2, 2, 1]))  # [1,2,1]
