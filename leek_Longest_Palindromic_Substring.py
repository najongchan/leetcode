class Solution:
    def isPalindrome(self, s):
        n = len(s)

        for k in range(n//2):
            if s[k] != s[-1-k]:
                return False
        return True

    def expandChecker(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        # answer = ''
        n = len(s)
        # max_len = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if self.isPalindrome(s[i:j+1]):
        #             # print(max_len)
        #             if max_len < j - i + 1:
        #                 max_len = j - i + 1
        #                 answer = s[i:j+1]

        start = end = 0
        for i in range(n):
            odd_len = self.expandChecker(s, i, i)
            even_len = self.expandChecker(s, i, i+1)
            length = max(odd_len, even_len)
            if length > (end - start):
                start = i - length//2
                end = i + length//2

        return s[start:end+1]
        
input = "babad"
temp = Solution()
print(temp.longestPalindrome(input))