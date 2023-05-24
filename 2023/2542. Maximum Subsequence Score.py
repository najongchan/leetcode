# https://leetcode.com/problems/maximum-subsequence-score/
from typing import List
from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        answer = total = 0
        heap = []

        pairs = zip(nums1, nums2)
        pairs = sorted(pairs, key=lambda x: -x[1])
        for num1, num2 in pairs:
            heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                answer = max(answer, total * num2)
        return answer

x = Solution()
print(x.maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3))
print(x.maxScore(nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1))
