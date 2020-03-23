# https://leetcode.com/problems/palindrome-partitioning/

class Solution(object):
    def partition(self, s):
        ret = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    ret.append([s[:i]]+rest)
        if not ret:
            return [[]]
        return ret