# https://leetcode.com/problems/map-sum-pairs/
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.keys = list()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        if key not in self.keys:
            self.keys.append(key)
        return

    def sum(self, prefix: str) -> int:
        # check key
        sum = 0
        for key in self.keys:
            try:
                if key.index(prefix) == 0:
                    sum += self.map[key]
            except:
                pass
        return sum

# Your MapSum object will be instantiated and called as such:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5

obj = MapSum()
obj.insert("apple", 3)
param_1 = obj.sum("ap")
obj.insert("app", 2)
param_2 = obj.sum("ap")
print(param_1)
print(param_2)