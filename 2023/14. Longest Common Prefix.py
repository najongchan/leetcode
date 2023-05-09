# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        left, right = strs[0], strs[-1]
        answer = ""
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                return answer
            answer += left[i]
        return answer

        # answer = ''
        # for i in range(len(strs[0])):
        #     for word in strs:
        #         if i == len(word) or word[i] != strs[0][i]:
        #             return answer
        #     answer += strs[0][i]
        #     print(i, answer)
        # return answer

x = Solution()
print(x.longestCommonPrefix(["flower","flow","flight"]))  # ['fl']
print(x.longestCommonPrefix(["dog","racecar","car"]))  # []
print(x.longestCommonPrefix(["a"]))  # []