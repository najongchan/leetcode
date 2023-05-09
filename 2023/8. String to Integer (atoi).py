# https://leetcode.com/problems/string-to-integer-atoi/
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # delete withspace
        to_int = re.findall('(^[-+]?[0]*\d+)\D*', s)
        print(to_int)
        if not to_int:
            return 0
        result = int(''.join(to_int))

        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        elif result < -1 * 2 ** 31:
            result = -1 * 2 ** 31
        return result


x = Solution()
print(x.myAtoi('+-12'))
print(x.myAtoi('words and 987'))
print(x.myAtoi('.1'))
