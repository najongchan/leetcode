# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        return True if re.search(pattern='^' + p + '$', string=s) else False
