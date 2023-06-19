# https://leetcode.com/problems/find-the-highest-altitude/
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = cur_altitude = 0
        for i in range(len(gain)):
            cur_altitude += gain[i]
            gain[i] = cur_altitude
            max_altitude = max(max_altitude, cur_altitude)
        return max_altitude
