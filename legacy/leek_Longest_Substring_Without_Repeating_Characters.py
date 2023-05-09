class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        repeat_check_set = set()
        i = 0
        j = 0
        answer = 0
        
        while i < length and j < length:
            if s[i] not in repeat_check_set:
                repeat_check_set.add(i)
                i += 1
                answer = max(answer, i - j)
            else:
                answer.remove(j)
                j += 1

        return answer