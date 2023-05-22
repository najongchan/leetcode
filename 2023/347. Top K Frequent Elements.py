# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        print(dictionary)
        answer = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

        return [element[0] for element in answer[:k]]


x = Solution()
print(x.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3], k=2))
