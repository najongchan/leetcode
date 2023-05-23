# https://leetcode.com/problems/longest-palindromic-substring/?envType=study-plan-v2&id=dynamic-programming
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.expandPalindrome(s, i, i)  # 홀수 길이 팰린드롬
            len2 = self.expandPalindrome(s, i, i + 1)  # 짝수 길이 팰린드롬
            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def expandPalindrome(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1


x = Solution()
print(x.longestPalindrome("babad"))
print(x.longestPalindrome("bb"))
