class Solution:
    def checkRefeat(self, s, start_point, end_point):
        check_list = []
        for i in range(start_point, end_point):
            if s[i] in check_list:
                return False
            else:
                check_list.append(s[i])
        return True
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.checkRefeat(s, i, j) == True:
                    answer = max(answer, j-i)
            
        return answer