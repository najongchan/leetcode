# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip = 0
        print(bin(a), bin(b), bin(c))
        while a or b or c:
            bit_a = a & 1   # rightest bit
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 0:
                flip += bit_a + bit_b
            else:
                flip += 1 - (bit_a or bit_b)

            a >>= 1
            b >>= 1
            c >>= 1

        return flip


x = Solution()
# print(x.minFlips(a=2, b=6, c=5))
# print(x.minFlips(a=4, b=2, c=7))
# print(x.minFlips(a=1, b=2, c=3))
print(x.minFlips(a=5, b=2, c=8))
