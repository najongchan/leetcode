# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        answer = 0
        left, right = 0, 1
        while right < len(s):
            if roman_map[s[left]] > roman_map[s[right]]:
                answer += roman_map[s[left]]
                left += 1
            elif roman_map[s[left]] == roman_map[s[right]]:
                right += 1
            elif roman_map[s[left]] < roman_map[s[right]]:
                temp = 0
                for i in s[left:right]:
                    temp -= roman_map[i]
                temp += roman_map[s[right]]
                answer += temp
                left = right + 1
                right += 2
        for i in s[left:right]:
            answer += roman_map[i]
        return answer

        # answer = 0
        # for i in range(len(s)-1):
        #     print(roman_map[s[i]], roman_map[s[i+1]])
        #     if roman_map[s[i]] < roman_map[s[i+1]]:
        #         answer -= roman_map[s[i]]
        #     else:
        #         answer += roman_map[s[i]]
        #     print(answer)
        # return answer + roman_map[s[-1]]


x = Solution()
print(x.romanToInt("III"))  # 3
print(x.romanToInt("LVIII"))  # 58
print(x.romanToInt("MCMXCIV"))  # 1994
print(x.romanToInt("MDCCCLXXXIV"))  # 1884
