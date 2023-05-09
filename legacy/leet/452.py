# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points) -> int:
        if len(points) <= 0:
            return 0

        points.sort(key=lambda x: x[1])
        arrowPos = points[0][1]
        cnt = 1
        for i in range(1, len(points)):
            if arrowPos >= points[i][0]:
                continue
            cnt += 1
            arrowPos = points[i][1]
        return cnt

t = [[10,16], [2,8], [1,6], [7,12]]
a = Solution()
print(a.findMinArrowShots(t))