# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0


x = Solution()
print(x.reverse(123))  # 321
print(x.reverse(120))  # 321
print(x.reverse(-123))  # -321

