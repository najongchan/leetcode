# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
from typing import List
from bisect import bisect_right

class Solution:
    def binarySearch(self, row, target):
        if target >= row[-1] or target < row[0]:
            return row[0]
        start, end = 0, len(row) - 1
        while start <= end:
            mid = (start + end) // 2
            if row[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        print(start)
        return start

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)]


x = Solution()
print(x.nextGreatestLetter(letters = ["c","f","j"], target = "c"))