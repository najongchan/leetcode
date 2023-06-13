# https://leetcode.com/problems/equal-row-and-column-pairs/
from collections import defaultdict
from typing import List
import numpy as np


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = defaultdict(int)
        count = 0
        for row in grid:
            row_dict[str(row)] += 1

        trans_grid = np.array(grid).transpose().tolist()
        for col in trans_grid:
            count += row_dict[str(col)]

        return count


x = Solution()
print(x.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
