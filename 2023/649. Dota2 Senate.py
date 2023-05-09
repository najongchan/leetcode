# https://leetcode.com/problems/dota2-senate/


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_list, d_list = [], []

        for i in range(n):
            if senate[i] == 'R':
                r_list.append(i)
            else:
                d_list.append(i)

        while r_list and d_list:
            r_index = r_list.pop(0)
            d_index = d_list.pop(0)

            if r_index < d_index:
                r_list.append(r_index + n)
            else:
                d_list.append(d_index + n)

        if r_list:
            return 'Radiant'
        else:
            return 'Dire'


x = Solution()
print(x.predictPartyVictory("RD"))  # Radiant
print(x.predictPartyVictory("RDD"))  # Dire
