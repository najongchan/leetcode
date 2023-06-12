# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def bin_sum(_mid):
            if _mid > index:
                _left = (_mid * 2 - index) * (index + 1) // 2
            else:
                _left = (_mid + 1) * _mid // 2 + (index - _mid + 1)

            if _mid > n - index - 1:
                _right = (_mid * 2 - n + index + 1) * (n - index) // 2
            else:
                _right = (_mid + 1) * mid // 2 + (n - index - _mid)

            return _left + _right - _mid

        left, right = 1, maxSum
        while left <= right:
            mid = (left + right) // 2
            if bin_sum(mid) <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        return right

x = Solution()
print(x.maxValue(n=6, index=1, maxSum=10))
print(x.maxValue(n=7, index=5, maxSum=30))
