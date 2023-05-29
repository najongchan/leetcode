# https://leetcode.com/problems/h-index/?envType=study-plan-v2&id=top-interview-150
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_index = 0
        for h in range(1, len(citations)):
            if citations[h] > citations[h-1]:
                if len(citations[:h]) > h - 1:
                    h_index = max(h_index, h - 1)
        return h_index