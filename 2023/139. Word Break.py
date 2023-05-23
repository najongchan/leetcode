# https://leetcode.com/problems/word-break/?envType=study-plan-v2&id=dynamic-programming
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


x = Solution()
print(x.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(x.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(x.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
